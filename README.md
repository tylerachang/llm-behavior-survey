# llm-behavior-survey
Webpage for the paper: [Language Model Behavior: A Comprehensive Survey](https://arxiv.org/abs/2303.11504) (Computational Linguistics, 2023).

See paper for discussion and details on each section. Links to citations are included below.

### Abstract
Transformer language models have received widespread public attention, yet their generated text is often surprising even to NLP researchers.
In this survey, we discuss over 250 recent studies of English language model behavior before task-specific fine-tuning.
Language models possess basic capabilities in syntax, semantics, pragmatics, world knowledge, and reasoning, but these capabilities are sensitive to specific inputs and surface features.
Despite dramatic increases in generated text quality as models scale to hundreds of billions of parameters, the models are still prone to unfactual responses, commonsense errors, memorized text, and social biases.
Many of these weaknesses can be framed as over-generalizations or under-generalizations of learned patterns in text.
We synthesize recent results to highlight what is currently known about large language model capabilities, thus providing a resource for applied work and for research in adjacent fields that use language models.

### Contents
* Transformer language models
* Syntax
* Semantics and pragmatics
* Commonsense and world knowledge
* Logical and numerical reasoning
* Memorized vs. novel text
* Bias, privacy, and toxicity
* Misinformation, personality, and politics

### Citation
<pre>
@article{chang-bergen-2023-language,
  title={Language Model Behavior: A Comprehensive Survey},
  author={Tyler A. Chang and Benjamin K. Bergen},
  journal={Computational Linguistics},
  year={2023},
  url={https://arxiv.org/abs/2303.11504},
}
</pre>

---

### Transformer Language Models
<details>
<summary>Architectures</summary>

The basic Transformer language model architecture has remained largely unchanged since 2018 ([Radford et al., 2018](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf); [Devlin et al., 2019](https://aclanthology.org/N19-1423/)).
First, an input text string is converted into a sequence of tokens, roughly corresponding to words.
Each token is mapped to a fixed vector "embedding"; the embedding for each token is learned during the pre-training process.
The sequence of embeddings is passed through a stack of Transformer layers that essentially mix the embeddings between tokens (using "self-attention"; [Vaswani et al. 2017](https://arxiv.org/abs/1706.03762)).
This mixing results in a "contextualized" vector representation for each token (e.g. a representation for the word "<i>dog</i>" in the context "<i>I saw a dog</i>").
Finally, after the stack of Transformer layers, each output token representation is projected into a distribution over the same token vocabulary used in the input.
In other words, the overall architecture maps each input token to a probability distribution over output tokens (e.g. the next token).
</details>

<details>
<summary>Training</summary>

Language modeling refers to predicting tokens (roughly equivalent to words) from context, usually text.
Masked and autoregressive language models are "pre-trained" to predict masked (i.e. hidden, fill-in-the-blank) or upcoming tokens respectively.
Popular recent language models (e.g. [ChatGPT](https://chat.openai.com/)) are primarily autoregressive language models; for each input token, the model produces a probability distribution over the next token (i.e. predicting each next token, which can be used for text generation).
These models are trained to maximize the probability of each next token.

Language models are pre-trained using gradient descent, observing many examples of plain text.
Due to high computational costs, relatively few language models are pre-trained from scratch, and they are usually trained in industry labs.
In practice, most NLP researchers build applications upon existing pre-trained language models.
Recent language models often contain further non-task-specific fine-tuning stages, such as additional training on examples that correctly follow instructions ("instruction tuning"; [Wei et al., 2022](https://arxiv.org/abs/2109.01652)), or reinforcement learning based on human preferences ("RLHF"; [Ouyang et al., 2022](https://arxiv.org/abs/2203.02155)).
We focus on non-fine-tuned language models, which still serve as the foundation for more recent language models.
</details>

### Syntax

<details>
<summary>Language models generally produce grammatical text, adhering to a wide variety of syntactic rules.</summary>

Citations: [Warstadt et al. (2020)](https://aclanthology.org/2020.tacl-1.25); [Hu et al. (2020)](https://aclanthology.org/2020.acl-main.158); [Gauthier et al. (2020)](https://aclanthology.org/2020.acl-demos.10); [Park et al. (2021)](https://www.proquest.com/scholarly-journals/deep-learning-can-contrast-minimal-pairs/docview/2574466437/se-2); [Wilcox et al. (2022)](https://doi.org/10.1162/ling\_a\_00491); [Hu et al. (2020)](https://aclanthology.org/2020.scil-1.39); [Warstadt et al. (2019)](https://aclanthology.org/D19-1286); [Lee and Schuster (2022)](https://aclanthology.org/2022.scil-1.18); [Perez-Mayos et al. (2021)](https://aclanthology.org/2021.emnlp-main.118); [Mahowald (2023)](http://arxiv.org/abs/2301.12564v2); [Zhang et al. (2022)](https://aclanthology.org/2022.blackboxnlp-1.24).
</details>

<details>
<summary>They learn subject-verb agreement, but they are sensitive to intervening clauses and specific words.</summary>

Citations: [van Schijndel et al. (2019)](https://aclanthology.org/D19-1592); [Goldberg (2019)](http://arxiv.org/abs/1901.05287v1); [Bacon and Regier (2019)](http://arxiv.org/abs/1908.09892v1); [Ryu and Lewis (2021)](https://aclanthology.org/2021.cmcl-1.6); [Lakretz et al. (2022)](https://aclanthology.org/2022.coling-1.285); [Lampinen (2022)](http://arxiv.org/abs/2210.15303v3); [Yu et al. (2020)](https://aclanthology.org/2020.emnlp-main.331); [Chaves and Richter (2021)](https://aclanthology.org/2021.scil-1.3); [Newman et al. (2021)](https://aclanthology.org/2021.naacl-main.290); [Wei et al. (2021)](https://aclanthology.org/2021.emnlp-main.72); [Lasri et al. (2022)](https://aclanthology.org/2022.findings-acl.181); [Lasri et al. (2022)](https://aclanthology.org/2022.coling-1.4).
</details>

<details>
<summary>They learn syntactic rules early in pre-training.</summary>

Citations: [Liu et al. (2021)](https://aclanthology.org/2021.findings-emnlp.71); [Zhang et al. (2021)](https://aclanthology.org/2021.acl-long.90); [Huebner et al. (2021)](https://aclanthology.org/2021.conll-1.49); [Choshen et al. (2022)](https://aclanthology.org/2022.acl-long.568); [Misra (2022)](http://arxiv.org/abs/2203.13112v1); [Chang and Bergen (2022)](https://aclanthology.org/2022.tacl-1.1).
</details>

<details>
<summary>They can learn word order without explicit position information, but word order is not necessary in many examples.</summary>

Citations: [Sinha et al. (2021)](https://aclanthology.org/2021.emnlp-main.230); [Abdou et al. (2022)](https://aclanthology.org/2022.acl-long.476); [Haviv et al. (2022)](https://aclanthology.org/2022.findings-emnlp.99); [Chang et al. (2021)](https://aclanthology.org/2021.acl-long.333); [Lasri et al. (2022)](https://aclanthology.org/2022.emnlp-main.118); [Wettig et al. (2023)](https://arxiv.org/abs/2202.08005); [Malkin et al. (2021)](https://aclanthology.org/2021.emnlp-main.809); [Sinha et al. (2022)](https://aclanthology.org/2022.findings-emnlp.326).
</details>

### Semantics and Pragmatics

<details>
<summary>Language models learn semantic and compositional properties of individual words, including argument structure, synonyms, and hypernyms (i.e. lexical semantics).</summary>

Citations: [Senel and Schutze (2021)](https://aclanthology.org/2021.eacl-main.42); [Hanna and Marecek (2021)](https://aclanthology.org/2021.blackboxnlp-1.20); [Ravichander et al. (2020)](https://aclanthology.org/2020.starsem-1.10); [Misra et al. (2021)](https://arxiv.org/abs/2105.02987); [Arefyev et al. (2020)](https://aclanthology.org/2020.coling-main.107); [Warstadt et al. (2020)](https://aclanthology.org/2020.tacl-1.25); [Davis and van Schijndel (2020)](https://aclanthology.org/2020.conll-1.32); [Upadhye et al. (2020)](https://aclanthology.org/2020.emnlp-main.70); [Kementchedjhieva et al. (2021)](https://aclanthology.org/2021.findings-acl.429); [Huynh et al. (2022)](https://arxiv.org/abs/2212.04348); [Hawkins et al. (2020)](https://aclanthology.org/2020.emnlp-main.376).
</details>

<details>
<summary>They struggle with negation, often performing worse as models scale.</summary>

Citations: [Ettinger (2020)](https://aclanthology.org/2020.tacl-1.3); [Kassner and Schutze (2020)](https://aclanthology.org/2020.acl-main.698); [Michaelov and Bergen (2022)](http://arxiv.org/abs/2212.08700v2); [Gubelmann and Handschuh (2022)](https://aclanthology.org/2022.acl-long.315); [Jang et al. (2022)](http://arxiv.org/abs/2209.12711v1).
</details>

<details>
<summary>They construct coherent but brittle situation models.</summary>

Citations: [Schuster and Linzen (2022)](https://aclanthology.org/2022.naacl-main.71); [Pandit and Hou (2021)](https://aclanthology.org/2021.naacl-main.327); [Zhang et al. (2023)](http://arxiv.org/abs/2301.10896v3); [Summers-Stay et al. (2021)](https://aclanthology.org/2021.mrqa-1.7).
</details>

<details>
<summary>They recognize basic analogies, metaphors, and figurative language.</summary>

Citations: [Pedinotti et al. (2021)](https://aclanthology.org/2021.blackboxnlp-1.13); [Griciute et al. (2022)](https://aclanthology.org/2022.flp-1.25); [Comsa et al. (2022)](https://aclanthology.org/2022.aacl-short.46); [Liu et al. (2022)](https://aclanthology.org/2022.naacl-main.330); [He et al. (2022)](https://aclanthology.org/2022.acl-long.543); [Ushio et al. (2021)](https://aclanthology.org/2021.acl-long.280); [Czinczoll et al. (2022)](https://aclanthology.org/2022.findings-emnlp.153); [Bhavya et al. (2022)](https://aclanthology.org/2022.inlg-main.25); [Weissweiler et al. (2022)](https://aclanthology.org/2022.emnlp-main.746).
</details>

<details>
<summary>They can infer the mental states of characters in text.</summary>

Citations: [Summers-Stay et al. (2021)](https://aclanthology.org/2021.mrqa-1.7); [Sap et al. (2022)](https://aclanthology.org/2022.emnlp-main.248); [Lal et al. (2022)](https://aclanthology.org/2022.emnlp-main.79); [Hu et al. (2022)](http://arxiv.org/abs/2212.06801v2); [Trott et al. (2022)](http://arxiv.org/abs/2209.01515v3); [Masis and Anderson (2021)](https://aclanthology.org/2021.blackboxnlp-1.8).
</details>

<details>
<summary>They struggle with implied meaning and pragmatics.</summary>

Citations: [Beyer et al. (2021)](https://aclanthology.org/2021.naacl-main.328); [Ruis et al. (2022)](https://arxiv.org/abs/2210.14986); [Cong (2022)](https://aclanthology.org/2022.csrr-1.3); [Kabbara and Cheung (2022)](https://aclanthology.org/2022.coling-1.65); [Kim et al. (2022)](https://aclanthology.org/2022.coling-1.72).
</details>

### Commonsense and World Knowledge

<details>
<summary>Language models learn facts and commonsense properties of objects, particularly as models scale.</summary>

Citations: [Davison et al. (2019)](https://aclanthology.org/D19-1109); [Petroni et al. (2019)](https://aclanthology.org/D19-1250); [Penha and Hauff (2020)](https://doi.org/10.1145/3383313.3412249); [Jiang et al. (2020)](https://aclanthology.org/2020.tacl-1.28); [Adolphs et al. (2021)](https://arxiv.org/abs/2108.01928); [Kalo and Fichtel (2022)](https://www.akbc.ws/2022/assets/pdfs/15_kamel_knowledge_analysis_with_.pdf); [Lin et al. (2020)](https://aclanthology.org/2020.emnlp-main.557); [Peng et al. (2022)](https://aclanthology.org/2022.emnlp-main.335); [Misra et al. (2023)](http://arxiv.org/abs/2210.01963v4); [Sahu et al. (2022)](http://arxiv.org/abs/2209.15093v1); [Kadavath et al. (2022)](https://arxiv.org/abs/2207.05221).
</details>

<details>
<summary>They are less sensitive than people to physical properties.</summary>

Citations: [Apidianaki and Gari Soler (2021)](https://aclanthology.org/2021.blackboxnlp-1.7); [Weir et al. (2020)](http://arxiv.org/abs/2004.04877v2); [Paik et al. (2021)](https://aclanthology.org/2021.emnlp-main.63); [Liu et al. (2022)](https://aclanthology.org/2022.aacl-short.27); [Shi and Wolff (2021)](https://escholarship.org/uc/item/0kr3t179); [De Bruyn et al. (2022)](https://aclanthology.org/2022.blackboxnlp-1.7); [Jiang and Riloff (2021)](https://aclanthology.org/2021.acl-long.540); [Jones et al. (2022)](https://escholarship.org/uc/item/44z7r3j3); [Stevenson et al. (2022)](http://arxiv.org/abs/2206.08932v1).
</details>

<details>
<summary>Learned facts are sensitive to context.</summary>

Citations: [Elazar et al. (2021)](https://aclanthology.org/2021.tacl-1.60); [Cao et al. (2022)](https://aclanthology.org/2022.acl-long.398); [Podkorytov et al. (2021)](https://ieeexplore.ieee.org/document/9534299); [Cao et al. (2021)](https://aclanthology.org/2021.acl-long.146); [Kwon et al. (2019)](http://arxiv.org/abs/1911.03024v1); [Beloucif and Biemann (2021)](https://aclanthology.org/2021.findings-emnlp.218); [Lin et al. (2020)](https://aclanthology.org/2020.emnlp-main.557); [Poerner et al. (2019)](https://arxiv.org/pdf/1911.03681v1.pdf); [Pandia and Ettinger (2021)](https://aclanthology.org/2021.emnlp-main.119); [Kassner and Sch{"u}tze (2020)](https://aclanthology.org/2020.acl-main.698); [Elazar et al. (2022)](http://arxiv.org/abs/2207.14251v2).
</details>

<details>
<summary>Learned facts are also sensitive to a fact's frequency in the pre-training corpus.</summary>

Citations: [Kassner et al. (2020)](https://aclanthology.org/2020.conll-1.45); [Kandpal et al. (2022)](https://arxiv.org/abs/2211.08411); [Mallen et al. (2022)](http://arxiv.org/abs/2212.10511v4); [Romero and Razniewski (2022)](https://aclanthology.org/2022.emnlp-main.752).
</details>

<details>
<summary>Factual knowledge continues to evolve late in pre-training.</summary>

Citations: [Chiang et al. (2020)](https://aclanthology.org/2020.emnlp-main.553); [Swamy et al. (2021)](https://openreview.net/forum?id=PW4AGjla3sx); [Liu et al. (2021)](https://aclanthology.org/2021.findings-emnlp.71); [Zhang et al. (2021)](https://aclanthology.org/2021.acl-long.90); [Porada et al. (2022)](https://aclanthology.org/2022.naacl-main.337); [Misra et al. (2023)](http://arxiv.org/abs/2210.01963v4).
</details>

<details>
<summary>Language models have a limited but nontrivial ability to make commonsense inferences about actions and events.</summary>

Citations: [Cho et al. (2021)](https://aclanthology.org/2021.findings-acl.258); [Shwartz and Choi (2020)](https://aclanthology.org/2020.coling-main.605); [Beyer et al. (2021)](https://aclanthology.org/2021.naacl-main.328); [Kauf et al. (2022)](http://arxiv.org/abs/2212.01488v2); [Qin et al. (2021)](https://aclanthology.org/2021.acl-long.549); [Zhao et al. (2021)](https://aclanthology.org/2021.conll-1.6); [Li et al. (2022)](https://aclanthology.org/2022.emnlp-main.812); [Stammbach et al. (2022)](https://aclanthology.org/2022.wnu-1.6); [Jin et al. (2022)](https://aclanthology.org/2022.umios-1.10); [Tamborrino et al. (2020)](https://aclanthology.org/2020.acl-main.357); [Misra (2022)](http://arxiv.org/abs/2203.13112v1); [Pandia et al. (2021)](https://aclanthology.org/2021.conll-1.29); [Ko and Li (2020)](https://aclanthology.org/2020.inlg-1.8); [Lee et al. (2021)](https://aclanthology.org/2021.naacl-main.158); [Pedinotti et al. (2021)](https://aclanthology.org/2021.starsem-1.1); [Li et al. (2022)](https://openreview.net/forum?id=sS5hCtc-uQ); [Zhou et al. (2021)](https://aclanthology.org/2021.emnlp-main.598); [Sancheti and Rudinger (2022)](https://aclanthology.org/2022.starsem-1.1); [Aroca-Ouellette et al. (2021)](https://aclanthology.org/2021.findings-acl.404); [Jones and Bergen (2021)](https://escholarship.org/uc/item/2h89m00k).
</details>

### Logical and Numerical Reasoning

<details>
<summary>Large language models can perform basic logical reasoning when prompted.</summary>

Citations: [Wei et al. (2022)](https://openreview.net/forum?id=_VjQlMeSB_J); [Suzgun et al. (2022)](https://arxiv.org/abs/2210.09261); [Lampinen et al. (2022)](https://aclanthology.org/2022.findings-emnlp.38); [Webb et al. (2022)](http://arxiv.org/abs/2212.09196v3); [Han et al. (2022)](https://arxiv.org/abs/2209.00840); [Kojima et al. (2022)](https://openreview.net/forum?id=e2TBb5y0yFf); [Wang et al. (2022)](http://arxiv.org/abs/2212.10001v2); [Min et al. (2022)](https://aclanthology.org/2022.emnlp-main.759).
</details>

<details>
<summary>They still struggle with complex reasoning.</summary>

Citations: [Saparov and He (2023)](http://arxiv.org/abs/2210.01240v4); [Valmeekam et al. (2022)](http://arxiv.org/abs/2206.10498v3); [Press et al. (2022)](http://arxiv.org/abs/2210.03350v2); [Katz et al. (2022)](https://aclanthology.org/2022.findings-emnlp.188); [Betz et al. (2021)](http://arxiv.org/abs/2103.13033v1); [Dasgupta et al. (2022)](http://arxiv.org/abs/2207.07051v1).
</details>

<details>
<summary>They exhibit basic numerical and probabilistic reasoning abilities, but they are dependent on specific inputs.</summary>

Citations: [Brown et al. (2020)](https://proceedings.neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf); [Wang et al. (2021)](http://arxiv.org/abs/2108.06743v2); [Wallace et al. (2019)](https://aclanthology.org/D19-1534); [Jiang et al. (2020)](https://aclanthology.org/2020.findings-emnlp.235); [Fujisawa and Kanai (2022)](http://arxiv.org/abs/2211.07727v1); [Razeghi et al. (2022)](https://aclanthology.org/2022.findings-emnlp.59); [Stolfo et al. (2022)](http://arxiv.org/abs/2210.12023v3); [Shi et al. (2023)](http://arxiv.org/abs/2302.00093v3); [Hagendorff et al. (2022)](https://arxiv.org/abs/2212.05206v1); [Hendrycks et al. (2021)](http://arxiv.org/abs/2103.03874v2); [Binz and Schulz (2023)](http://arxiv.org/abs/2206.14576v1).
</details>

### Memorized vs. Novel Text

<details>
<summary>As language models scale, they are more likely to generate memorized text from the pre-training corpus.</summary>

Citations: [Carlini et al. (2021)](http://arxiv.org/abs/2012.07805v2); [Lee et al. (2022)](https://aclanthology.org/2022.acl-long.577); [Carlini et al. (2023)](http://arxiv.org/abs/2202.07646v3); [Kandpal et al. (2022)](http://arxiv.org/abs/2202.06539v3); [Hernandez et al. (2022)](http://arxiv.org/abs/2205.10487v1); [Lee et al. (2023)](https://arxiv.org/abs/2203.07618); [Ippolito et al. (2022)](http://arxiv.org/abs/2210.17546v2); [Tirumala et al. (2022)](https://openreview.net/forum?id=u3vEuRr08MT); [Kharitonov et al. (2021)](http://arxiv.org/abs/2110.02782v2).
</details>

<details>
<summary>They generate novel text that is consistent with the input context.</summary>

Citations: [Tuckute et al. (2022)](https://aclanthology.org/2022.naacl-demo.11); [McCoy et al. (2021)](http://arxiv.org/abs/2111.09509v1); [Meister and Cotterell (2021)](https://aclanthology.org/2021.acl-long.414); [Chiang and Chen (2021)](https://aclanthology.org/2021.blackboxnlp-1.16); [Massarelli et al. (2020)](https://aclanthology.org/2020.findings-emnlp.22); [Cifka and Liutkus (2022)](http://arxiv.org/abs/2212.14815v3); [Dou et al. (2022)](https://aclanthology.org/2022.acl-long.501); [Sinclair et al. (2022)](https://aclanthology.org/2022.tacl-1.60); [Sinha et al. (2022)](http://arxiv.org/abs/2212.08979v1); [Aina and Linzen (2021)](https://aclanthology.org/2021.blackboxnlp-1.4); [Reif et al. (2022)](https://aclanthology.org/2022.acl-short.94); [O'Connor and Andreas (2021)](https://aclanthology.org/2021.acl-long.70); [Misra et al. (2020)](https://aclanthology.org/2020.findings-emnlp.415); [Michaelov and Bergen (2022)](https://aclanthology.org/2022.conll-1.2); [Armeni et al. (2022)](https://aclanthology.org/2022.conll-1.28).
</details>

### Bias, Privacy, and Toxicity

<details>
<summary>Language models sometimes generate offensive text and hate speech, particularly in response to targeted prompts.</summary>

Citations: [Ganguli et al. (2022)](http://arxiv.org/abs/2209.07858v2); [Gehman et al. (2020)](https://aclanthology.org/2020.findings-emnlp.301); [Wallace et al. (2019)](https://aclanthology.org/D19-1221); [Heidenreich and Williams (2021)](https://doi.org/10.1145/3461702.3462578); [Mehrabi et al. (2022)](https://aclanthology.org/2022.naacl-main.204); [Perez et al. (2022)](https://aclanthology.org/2022.emnlp-main.225).
</details>

<details>
<summary>They can expose private information, but often not tied to specific individuals.</summary>

Citations: [Ganguli et al. (2022)](http://arxiv.org/abs/2209.07858v2); [Perez et al. (2022)](https://aclanthology.org/2022.emnlp-main.225); [Huang et al. (2022)](https://aclanthology.org/2022.findings-emnlp.148); [Lehman et al. (2021)](https://aclanthology.org/2021.naacl-main.73); [Shwartz et al. (2020)](https://aclanthology.org/2020.emnlp-main.556).
</details>

<details>
<summary>Language model performance varies across demographic groups.</summary>

Citations: [Smith et al. (2022)](https://aclanthology.org/2022.emnlp-main.625); [Brandl et al. (2022)](https://aclanthology.org/2022.naacl-main.265); [Zhang et al. (2021)](https://aclanthology.org/2021.emnlp-main.375); [Groenwold et al. (2020)](https://aclanthology.org/2020.emnlp-main.473); [Zhou et al. (2022)](https://aclanthology.org/2022.findings-acl.164).
</details>

<details>
<summary>Probabilities of toxic text vary across demographic groups.</summary>

Citations: [Hassan et al. (2021)](https://aclanthology.org/2021.findings-emnlp.267); [Ousidhoum et al. (2021)](https://aclanthology.org/2021.acl-long.329); [Nozza et al. (2022)](https://aclanthology.org/2022.ltedi-1.4); [Sheng et al. (2019)](https://aclanthology.org/D19-1339); [Magee et al. (2021)](http://arxiv.org/abs/2107.07691v1); [Dhamala et al. (2021)](https://doi.org/10.1145/3442188.3445924); [Sheng et al. (2021)](https://aclanthology.org/2021.acl-long.330); [Akyurek et al. (2022)](https://aclanthology.org/2022.gebnlp-1.9); [Kurita et al. (2019)](https://aclanthology.org/W19-3823); [Silva et al. (2021)](https://aclanthology.org/2021.naacl-main.189).
</details>

<details>
<summary>Language models reflect harmful group-specific stereotypes based on gender, sexuality, race, religion, and other demographic identities.</summary>

Citations: [Nangia et al. (2020)](https://aclanthology.org/2020.emnlp-main.154); [Kurita et al. (2019)](https://aclanthology.org/W19-3823); [Choenni et al. (2021)](https://aclanthology.org/2021.emnlp-main.111); [Nadeem et al. (2021)](https://aclanthology.org/2021.acl-long.416); [Nozza et al. (2021)](https://aclanthology.org/2021.naacl-main.191); [Felkner et al. (2022)](http://arxiv.org/abs/2206.11484v2); [Abid et al. (2021)](http://arxiv.org/abs/2101.05783v2); [Kirk et al. (2021)](https://proceedings.neurips.cc/paper/2021/file/1531beb762df4029513ebf9295e0d34f-Paper.pdf); [Bartl et al. (2020)](https://aclanthology.org/2020.gebnlp-1.1); [de Vassimon Manela et al. (2021)](https://aclanthology.org/2021.eacl-main.190); [Touileb (2022)](https://aclanthology.org/2022.aacl-short.53); [Alnegheimish et al. (2022)](https://aclanthology.org/2022.naacl-main.203); [Tal et al. (2022)](https://aclanthology.org/2022.gebnlp-1.13); [Srivastava et al. (2022)](https://arxiv.org/abs/2206.04615); [Tang and Jiang (2022)](http://arxiv.org/abs/2211.14639v1); [Seshadri et al. (2022)](https://openreview.net/forum?id=rIhzjia7SLa); [Mattern et al. (2022)](http://arxiv.org/abs/2212.10678v1); [Akyurek et al. (2022)](https://aclanthology.org/2022.gebnlp-1.9); [Shaikh et al. (2022)](https://arxiv.org/abs/2212.08061).
</details>

### Misinformation, Personality, and Politics

<details>
<summary>Language models can generate convincing unfactual text.</summary>

Citations: [Levy et al. (2021)](https://aclanthology.org/2021.findings-acl.416); [Lin et al. (2022)](https://aclanthology.org/2022.acl-long.229); [Rae et al. (2021)](https://arxiv.org/abs/2112.11446); [Raj et al. (2022)](http://arxiv.org/abs/2211.05853v2); [Heidenreich and Williams (2021)](https://doi.org/10.1145/3461702.3462578); [Spitale et al. (2023)](http://arxiv.org/abs/2301.11924v2); [Chen et al. (2022)](http://arxiv.org/abs/2209.13627v2).
</details>

<details>
<summary>They can generate unsafe advice.</summary>

Citations: [Zellers et al. (2021)](https://aclanthology.org/2021.naacl-main.386); [Chuang and Yang (2022)](https://aclanthology.org/2022.acl-short.12); [Levy et al. (2022)](https://aclanthology.org/2022.emnlp-main.154); [Jin et al. (2022)](https://openreview.net/forum?id=uP9RiC4uVcR).
</details>

<details>
<summary>Model-generated text is difficult to distinguish from human-generated text.</summary>

Citations: [Brown et al. (2020)](https://proceedings.neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf); [Wahle et al. (2022)](https://aclanthology.org/2022.emnlp-main.62); [Spitale et al. (2023)](http://arxiv.org/abs/2301.11924v2); [Ippolito et al. (2020)](https://aclanthology.org/2020.acl-main.164); [Clark et al. (2021)](https://aclanthology.org/2021.acl-long.565); [Dugan et al. (2023)](https://arxiv.org/abs/2212.12672); [Jakesch et al. (2023)](https://www.pnas.org/doi/abs/10.1073/pnas.2208839120); [Jawahar et al. (2020)](https://aclanthology.org/2020.coling-main.208); [Wahle et al. (2022)](https://aclanthology.org/2022.emnlp-main.62).
</details>

<details>
<summary>Language model "personality" and politics depend on the input context.</summary>

Citations: [Perez et al. (2022)](https://arxiv.org/abs/2212.09251); [Simmons (2022)](http://arxiv.org/abs/2209.12106v2); [Argyle et al. (2023)](http://arxiv.org/abs/2209.06899v1); [Liu et al. (2022)](https://www.sciencedirect.com/science/article/pii/S0004370221002058); [Johnson et al. (2022)](http://arxiv.org/abs/2203.07785v1); [Bang et al. (2021)](https://aclanthology.org/2021.sigdial-1.57); [Sheng et al. (2021)](https://aclanthology.org/2021.naacl-main.60); [Patel and Pavlick (2021)](https://aclanthology.org/2021.emnlp-main.790); [Chen et al. (2022)](http://arxiv.org/abs/2209.13627v2); [Caron and Srivastava (2022)](http://arxiv.org/abs/2212.10276v1); [Jiang et al. (2022)](http://arxiv.org/abs/2206.07550v2); [Li et al. (2022)](http://arxiv.org/abs/2212.10529v2); [Miotto et al. (2022)](https://aclanthology.org/2022.nlpcss-1.24); [Aher et al. (2022)](http://arxiv.org/abs/2208.10264v5).
</details>

### Discussion

See [full paper](https://arxiv.org/abs/2303.11504) for discussion on the effects of scale (model size), language modeling as generalization, and levels of analysis in understanding language models.
