import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords

docs = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(docs)

stop_words = set(stopwords.words("english"))

words = []
for w in movie_reviews.words():
    if w not in stop_words:
        words.append(w.lower())

words = nltk.FreqDist(words)
print(words.most_common(20))
