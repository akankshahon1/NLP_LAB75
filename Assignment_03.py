import gensim
from gensim.models.word2vec import Word2Vec
from multiprocessing import cpu_count
import gensim.downloader as api

dataset = api.load("text8")
words = [d for d in dataset]

data1 = words[:1000]
w2v_model = Word2Vec(data1, min_count = 0, workers=cpu_count())
print(w2v_model.wv.most_similar('social'))