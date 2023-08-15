"""
Generate a file of new papers, found since the last citation search. Finds
all papers that cite the list of seed ids. Also updates existing papers with
missing fields if possible.

Outputs:
paper_list_annotated_updated.tsv (old papers, with missing fields added)
new_paper_list.tsv (new papers)
unfiltered_ids_updated.txt (previously scraped ids, with new paper ids added)

Sample usage:
python3 scripts/update_paper_list.py

"""

import codecs
import pandas as pd
import requests
from tqdm import tqdm
import json
import time
from collections import defaultdict

# Semantic scholar ids of the papers in the seed.
SEED_IDS_INPATH = 'final_papers/seed_paper_ids.txt'
# The existing list of papers, filtered and with metadata.
PAPER_LIST_INPATH = 'final_papers/paper_list_annotated.tsv'
# The list of paper ids already scraped, unfiltered.
UNFILTERED_IDS_INPATH = 'final_papers/unfiltered_ids.txt'

# See outputs in description.
PAPER_LIST_OUTPATH = 'final_papers/paper_list_annotated_updated.tsv'
NEW_PAPER_LIST_OUTPATH = 'final_papers/new_paper_list.tsv'
UNFILTERED_IDS_OUTPATH = 'final_papers/unfiltered_ids_updated.txt'


# Get seed ids.
seed_ids = []
infile = codecs.open(SEED_IDS_INPATH, 'rb', encoding='utf-8')
for line in infile:
    id = line.strip()
    if id:
        seed_ids.append(id)
infile.close()

# Get unfiltered paper ids. These are skipped when getting citations.
unfiltered_ids = []
infile = codecs.open(UNFILTERED_IDS_INPATH, 'rb', encoding='utf-8')
for line in infile:
    id = line.strip()
    if id:
        unfiltered_ids.append(id)
infile.close()


# Make a Semantic Scholar request using a URL query.
def scholar_request(query):
    first_try = True
    parsed_response = None
    try:
        response = requests.get(query, timeout=None)
        parsed_response = json.loads(response.text)
    except:
        print('Failed request: {}'.format(query))
    # Regardless of the case above, wait and retry if necessary.
    while parsed_response is None or ('message' in parsed_response and parsed_response['message'] == 'Too Many Requests'):
        first_try = False
        print('Error; this may be due to rate limits; waiting...')
        time.sleep(65) # Wait 65 seconds.
        try:
            response = requests.get(query, timeout=None)
            parsed_response = json.loads(response.text)
        except:
            # Note: will keep retrying.
            print('Failed request: {}'.format(query))
    if not first_try:
        print('Succeeded after waiting.')
    if 'message' in parsed_response and parsed_response['message'] == 'Internal Server Error':
        print('WARNING: internal server error for request: {}'.format(query))
        return None
    # Set the default value to the empty string.
    to_pop = []
    for key, value in parsed_response.items():
        if value is None:
            to_pop.append(key)
    for key in to_pop:
        parsed_response.pop(key)
    parsed_response = defaultdict(lambda: '', parsed_response)
    return parsed_response

# Return an updated row dict given an existing row dict.
FIELDS = ['title', 'year', 'url', 'abstract', 'semanticscholar_tldr',
          'citation_count', 'semanticscholar_id', 'bibtex']
def update_paper_dict(paper_dict):
    # Check if already has all fields.
    has_all_fields = True
    for field in FIELDS:
        if field not in paper_dict or str(paper_dict[field]).strip() == '':
            has_all_fields = False
    if has_all_fields:
        return paper_dict
    if 'semanticscholar_id' not in paper_dict:
        print('WARNING: no paper id; cannot update paper dict.')
        return paper_dict
    # Otherwise, run query.
    paper_id = paper_dict['semanticscholar_id']
    query = 'https://api.semanticscholar.org/graph/v1/paper/{}'.format(paper_id)
    query += '?fields=title,year,url,abstract,tldr,citationCount,citationStyles,authors'
    response = scholar_request(query)
    if response is None:
        print('WARNING: failed request; cannot update paper dict.')
        return paper_dict
    # Update row.
    retrieved = defaultdict(lambda: '')
    retrieved['title'] = response['title'].strip()
    retrieved['year'] = response['year']
    retrieved['url'] = response['url'].strip()
    retrieved['citation_count'] = response['citationCount']
    retrieved['semanticscholar_id'] = response['paperId'].strip()
    retrieved['abstract'] = ' '.join(response['abstract'].strip().split())
    # Process tldr.
    retrieved['semanticscholar_tldr'] = ''
    if response['tldr']:
        retrieved['semanticscholar_tldr'] = ' '.join(response['tldr']['text'].strip().split())  # Convert white spaces to space.

    # Process bibtex.
    if 'bibtex' in response['citationStyles']:
        bibtex = response['citationStyles']['bibtex'].strip()
        key_start = bibtex.index('{') + 1 # Inclusive.
        key_end = bibtex.split('{')[1].index('\n')-1 + key_start # Exclusive. First newline after opening brace, then exclude the comma immediately preceding.
        bibtex_prefix = bibtex[:key_start]
        bibtex_suffix = bibtex[key_end:]
        bibtex_key = bibtex[key_start:key_end]
        if bibtex_suffix[0] != ',':
            print('WARNING: comma not immediately after bib key; may have been parsed incorrectly.')
        if '=' in bibtex_key:
            print('WARNING: found \'=\' in bib key; may have been parsed incorrectly.')

        # Create bibtex key.
        split_title = retrieved['title'].replace('-', ' ').strip().lower().split()
        title_first_word = split_title[0] if len(split_title) > 0 else ''
        authors = [author['name'].replace('-', ' ').strip().split()[-1].lower() for author in response['authors']]
        # Start with first author if available.
        updated_key = authors[0] if len(authors) > 0 else ''
        if len(authors) == 2: # Add other author(s).
            updated_key = updated_key + '-' + authors[1]
        elif len(authors) > 2:
            updated_key = updated_key + '-etal'
        # Then year if available.
        if str(retrieved['year']):
            updated_key = updated_key + '-' if updated_key else ''
            updated_key = updated_key + str(response['year']).replace('-', '')
        # Then title first word, or untitled.
        updated_key = updated_key + '-' if updated_key else ''
        if title_first_word == '':
            updated_key = updated_key + 'untitled'
        else:
            updated_key = updated_key + title_first_word
        # Bib keys cannot contain commas.
        updated_key = updated_key.replace(',', '')
        bibtex = bibtex_prefix + updated_key + bibtex_suffix
        retrieved['bibtex'] = bibtex

    # Update any empty fields in paper dict.
    # Note: any other fields will be retained.
    for field in FIELDS:
        if field not in paper_dict or str(paper_dict[field]).strip() == '':
            paper_dict[field] = retrieved[field]
    return paper_dict

# Update a papers data frame.
def update_papers_df(df):
    for row_i, row in tqdm(df.iterrows()):
        paper_dict = dict(row)
        paper_dict = update_paper_dict(paper_dict)
        df.iloc[row_i] = paper_dict
    df = df.fillna('')
    return df

# Get citations to a list of seed ids.
# Returns a papers df populated only with ids and titles. Remaining columns will be empty.
def get_citations_df(seed_ids, skip_ids=[], columns=[]):
    new_ids = []
    citations_df = pd.DataFrame(columns=columns)
    for paper_id in tqdm(seed_ids):
        query = 'https://api.semanticscholar.org/graph/v1/paper/{}'.format(paper_id)
        query += '?fields=citations.title,citations.paperId'
        response = scholar_request(query)
        citations = response['citations']
        for cite_paper in citations:
            cite_id = cite_paper['paperId']
            cite_title = cite_paper['title'] if 'title' in cite_paper else ''
            # Add to citations_df.
            if cite_id not in list(seed_ids) + list(skip_ids) + list(new_ids):
                new_ids.append(cite_id)
                row_dict = {'semanticscholar_id': cite_id, 'title': cite_title}
                citations_df = citations_df.append(row_dict, ignore_index=True)
    citations_df = citations_df.fillna('')
    return citations_df


# Get citations. Set headers to be same as papers df.
papers_df = pd.read_csv(PAPER_LIST_INPATH, sep='\t', encoding='utf-8', keep_default_na=False)
columns = list(papers_df.columns)
print('Getting new citations.')
new_papers_df = get_citations_df(seed_ids, skip_ids=unfiltered_ids, columns=columns)
print('Found {} new citations.'.format(new_papers_df.shape[0]))

# Populate new papers df and save.
print('Populating new paper info.')
new_papers_df = update_papers_df(new_papers_df)
new_papers_df.to_csv(NEW_PAPER_LIST_OUTPATH, sep='\t', index=False, encoding='utf-8')
print('Saved new papers df.')

# Save updated unfiltered ids.
unfiltered_ids_updated = unfiltered_ids + list(new_papers_df['semanticscholar_id'])
outfile = codecs.open(UNFILTERED_IDS_OUTPATH, 'wb', encoding='utf-8')
for id in unfiltered_ids_updated:
    outfile.write(id.strip())
    outfile.write('\n')
outfile.close()
del new_papers_df
print('Saved updated ids.')

# Just in case, populate old papers df and save.
print('Populating original paper info.')
papers_df = update_papers_df(papers_df)
papers_df.to_csv(PAPER_LIST_OUTPATH, sep='\t', index=False, encoding='utf-8')
print('Saved original papers df updated.')
print('Done.')
