import gensim
import pprint
import numpy as np
from gensim import corpora,models
from gensim.utils import simple_preprocess
text = ["The food is excellent but the service can be better",
        "The food is always delicious and loved the service",
        "The food was mediocre and the service was terrible"]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')
print(" ")
print("TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])
    
    
#output
"""Dictionary : 
[['be', 1], ['better', 1], ['but', 1], ['can', 1], ['excellent', 1], ['food', 1], ['is', 1], ['service', 1], ['the', 2]]
[['food', 1], ['is', 1], ['service', 1], ['the', 2], ['always', 1], ['and', 1], ['delicious', 1], ['loved', 1]]
[['food', 1], ['service', 1], ['the', 2], ['and', 1], ['mediocre', 1], ['terrible', 1], ['was', 2]]
TF-IDF Vector:
[['be', 0.43], ['better', 0.43], ['but', 0.43], ['can', 0.43], ['excellent', 0.43], ['food', 0.09], ['is', 0.21], ['service', 0.09], ['the', 0.18]]
[['food', 0.11], ['is', 0.26], ['service', 0.11], ['the', 0.21], ['always', 0.52], ['and', 0.26], ['delicious', 0.52], ['loved', 0.52]]
[['food', 0.08], ['service', 0.08], ['the', 0.16], ['and', 0.2], ['mediocre', 0.39], ['terrible', 0.39], ['was', 0.78]]
"""
