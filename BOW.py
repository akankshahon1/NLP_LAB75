#Assignment no 2
#Name:Akansha Hon
#Roll no:75
#Batch:B4
#Assignment name:Implementation of Bag of words to find the frequency of the tokens
from gensim.utils import simple_preprocess
from gensim import corpora

#text2 = open('sample_text.txt', encoding='utf-8')

text2 = ["""Hello, how are you?", "How do you do?", 
   "Hey what are you doing? yes you What are you doing?"""]

tokens2 = []
# for line in text2.read().split('.'):
for line in text2[0].split('.'):
    tokens2.append(simple_preprocess(line, deacc=True))

g_dict2 = corpora.Dictionary(tokens2)

print("The dictionary has: " + str(len(g_dict2)) + " tokens")
print(g_dict2.token2id)
print("\n")

g_bow =[g_dict2.doc2bow(token, allow_update = True) for token in tokens2]
print("Bag of Words : ", g_bow)





#OUTPUT:
#[[(0, 1), (1, 1), (2, 1), (3, 1)], [(2, 1), (3, 1), (4, 2)], [(0, 2), (3, 3), (5, 2), (6, 1), (7, 2), (8, 1)]]
#[[('are', 1), ('hello', 1), ('how', 1), ('you', 1)], [('how', 1), ('you', 1), ('do', 2)], [('are', 2), ('you', 3), ('doing', 2), ('hey', 1), ('what', 2), ('yes', 1)]]