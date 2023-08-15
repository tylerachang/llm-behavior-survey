"""
Creates the bib file from the paper list. Manages key collisions.

Sample usage:
python3 scripts/create_bibtex.py

"""

import codecs
import pandas as pd

PAPER_LIST_INPATH = 'final_papers/paper_list_annotated.tsv'
BIB_OUTPATH = 'final_papers/paper_list.bib'


papers_df = pd.read_csv(PAPER_LIST_INPATH, sep='\t', encoding='utf-8', usecols=['title', 'bibtex'], keep_default_na=False)

def to_alphanumeric(input, allow_space=False, allow_dash=False):
    if allow_space:
        input = ' '.join(input.strip().split()) # Convert all whitespace to one space.
    chars = [ch for ch in input if ch.isalnum() or (ch == ' ' and allow_space) or (ch == '-' and allow_dash)]
    return ''.join(chars)

print('Getting initial values.')
# Get the initial bibtex keys.
bib_prefixes = []
bib_keys = []
bib_suffixes = []
for bibtex in papers_df['bibtex']:
    if not bibtex:
        bib_prefixes.append('')
        bib_keys.append('')
        bib_suffixes.append('')
        continue
    # Get original prefix, key, and suffix.
    bibtex = bibtex.strip()
    key_start = bibtex.index('{') + 1 # Inclusive.
    key_end = bibtex.split('{')[1].index(',') + key_start # Exclusive. First comma after opening brace.
    bib_keys.append(bibtex[key_start:key_end])
    bib_suffixes.append(bibtex[key_end:])
    # Replace prefix "@...{" with "@article{".
    bib_prefix = bibtex[:key_start]
    to_replace = bib_prefix[1:bib_prefix.index('{')]
    bib_prefix = bib_prefix.replace(to_replace, 'article', 1)
    bib_prefixes.append(bib_prefix)
bib_keys = [to_alphanumeric(bib_key, allow_space=False, allow_dash=True) for bib_key in bib_keys]
# Corresponding titles.
titles = list(papers_df['title'])
split_titles = [to_alphanumeric(title, allow_space=True, allow_dash=False).strip().lower().split() for title in titles]
assert len(bib_keys) == len(split_titles)
assert len(bib_keys) == len(bib_prefixes)
assert len(bib_keys) == len(bib_suffixes)

print('Managing collisions.')
# Remove duplicates.
# Iterate through the bib keys.
for bib_i, bib_key1 in enumerate(bib_keys):
    if bib_key1 == '':
        # Key should only be empty for empty bib entries.
        assert bib_prefixes[bib_i] == ''
        assert bib_suffixes[bib_i] == ''
        continue
    if bib_key1 not in bib_keys[:bib_i] + bib_keys[bib_i+1:]:
        # No duplicates found.
        continue
    print('Duplicate found: {}'.format(bib_key1))
    # Find the duplicates.
    matching_indices = [bib_i]
    for bib_j, bib_key2 in enumerate(bib_keys):
        if bib_j == bib_i:
            continue
        if bib_key2 == bib_key1:
            matching_indices.append(bib_j)
    # Keep adding title words until they no longer match.
    curr_title_word = 1
    while True:
        # Add one title word to the keys.
        for match_i, paper_idx in enumerate(matching_indices):
            if curr_title_word < len(split_titles[paper_idx]):
                to_add = split_titles[paper_idx][curr_title_word]
            else:
                to_add = str(match_i)
            bib_keys[paper_idx] += '-' + to_add
        # Check for matches.
        new_keys = [bib_keys[paper_idx] for paper_idx in matching_indices]
        if len(new_keys) == len(set(new_keys)):
            # No more duplicates. Print.
            for new_key in new_keys:
                print('-> {}'.format(new_key))
            break
        curr_title_word += 1
# Sanity check.
nonempty_keys = [key for key in bib_keys if key != '']
assert len(nonempty_keys) == len(set(nonempty_keys))
print('Removed duplicates.')

print('Writing bib file.')
outfile = codecs.open(BIB_OUTPATH, 'wb', encoding='utf-8')
for i in range(len(bib_keys)):
    # New bibtex.
    to_write = bib_prefixes[i] + bib_keys[i] + bib_suffixes[i]
    if to_write == '':
        continue
    assert to_write[0] == '@'
    # Write.
    outfile.write(to_write)
    outfile.write('\n')
outfile.close()
print('Done.')
