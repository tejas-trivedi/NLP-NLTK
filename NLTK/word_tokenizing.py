from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

str1 = " White House organizing program to slash development time for coronavirus vaccine by as much as eight months"
str2 = "White House risks backlash with coronavirus optimism if cases flare up again."

stop_words = set(stopwords.words("english"))
filtered_sentence1 = []
filtered_sentence2 = []

for i in word_tokenize(str1):
    if i not in stop_words:
        filtered_sentence1.append(i)

print(filtered_sentence1)

for i in word_tokenize(str2):
    if i not in stop_words:
        filtered_sentence2.append(i)

print(filtered_sentence2)



