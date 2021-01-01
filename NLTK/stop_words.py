# Stopwords are the English words which does not add much meaning to a sentence.
# They can safely be ignored without sacrificing the meaning of the sentence.

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

str1 = "White House organizing program to slash development time for coronavirus vaccine by as much as eight months"
str2 = "White House risks backlash with coronavirus optimism if cases flare up again."

stop_words = set(stopwords.words("english"))

words1 = word_tokenize(str1)
words2 = word_tokenize(str2)

filtered_sentence1 = []
filtered_sentence2 = []

for w in words1:
    if w not in stop_words:
        filtered_sentence1.append(w)

print(filtered_sentence1)
print('\n')

for w in words2:
    if w not in stop_words:
        filtered_sentence2.append(w)

print(filtered_sentence2)
