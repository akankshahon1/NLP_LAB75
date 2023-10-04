from gensim.models.word2vec import Word2Vec
from multiprocessing import cpu_count

print("\n Word2vec \n")

data = [
    "Open Visual Studio Code.",
    "Import the NLTK library",
    "Apart from individual data packages",
    "word2vec is a popular word",
]

# Tokenize the text data (split sentences into words)
tokenized_data = [sentence.split() for sentence in data]

# Create a Word2Vec model
w2v_model = Word2Vec(tokenized_data, min_count=0, workers=cpu_count())

# Find the most similar words to 'word'
similar_words = w2v_model.wv.most_similar('word')

for word, score in similar_words:
    print(f"{word}: {score}")
    
#output
Word2vec 
"""
a: 0.21883945167064667
Apart: 0.21617142856121063
data: 0.0931011214852333
NLTK: 0.09291722625494003
individual: 0.07963486760854721
from: 0.06285078823566437
is: 0.05433003976941109
library: 0.0270574688911438
the: 0.016134677454829216
popular: -0.01083916611969471
"""