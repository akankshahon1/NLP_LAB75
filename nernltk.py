import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
nltk.download('treebank')
sent = nltk.corpus.treebank.tagged_sents()
print(nltk.ne_chunk(sent[0]))
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
raw_words= word_tokenize(raw_text)
tags=pos_tag(raw_words)
nltk.download('maxent_ne_chunker')
nltk.download('words')
ne = nltk.ne_chunk(tags,binary=True)
print(ne)
from nltk.chunk import tree2conlltags
iob = tree2conlltags(ne)
iob

