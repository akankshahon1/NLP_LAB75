#Assignment no 2
#Name:Akanksha Hon
#Roll no:75
#Batch:B4
#Assignment name:Implementation of Bag of words to find the frequency of the tokens
from gensim import corpora
from gensim.utils import simple_preprocess
doc_list = [
   "Hello, how are you?", "How do you do?", 
   "Hey what are you doing? yes you What are you doing?"
]
#Do the tokenization
doc_tokenized = [simple_preprocess(doc) for doc in doc_list]
dictionary = corpora.Dictionary()
#for bag of words
BoW_corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in doc_tokenized]
#print bag of words
print(BoW_corpus)
#convert id to tokens/words
id_words = [[(dictionary[id], count) for id, count in line] for line in BoW_corpus]
print(id_words)


#OUTPUT:
[[(0, 1), (1, 1), (2, 1), (3, 1)], [(2, 1), (3, 1), (4, 2)], [(0, 2), (3, 3), (5, 2), (6, 1), (7, 2), (8, 1)]]
[[('are', 1), ('hello', 1), ('how', 1), ('you', 1)], [('how', 1), ('you', 1), ('do', 2)], [('are', 2), ('you', 3), ('doing', 2), ('hey', 1), ('what', 2), ('yes', 1)]]