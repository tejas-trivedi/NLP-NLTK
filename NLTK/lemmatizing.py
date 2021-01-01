# Lemmatization is the process of grouping together the different inflected forms of a word so they can be analysed as a single item.
# Lemmatization is similar to stemming but it links words with similar meaning to one word

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import  word_tokenize

#file =  open('text.txt', 'r') 
#data=file.read().replace('\n', '')
data1 = " White House organizing program to slash development time for coronavirus vaccine by as much as eight months"
data2 = "White House risks backlash with coronavirus optimism if cases flare up again."

lemmatizer  =  WordNetLemmatizer()
lemma_sentence1 = []
lemma_sentence2 = []


for i in word_tokenize(data1):
    lemma_sentence1.append(lemmatizer.lemmatize(i))
print(lemma_sentence1)
print('\n')

for i in word_tokenize(data2): 
    lemma_sentence2.append(lemmatizer.lemmatize(i))
print(lemma_sentence2)


