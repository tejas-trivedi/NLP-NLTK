# Steming is a method to find root of any word. The part of the word which actually gives sense of the word

from nltk.stem import PorterStemmer        # The Porter stemming algorithm is a process for removing the commoner morphological endings from words in English.
from nltk.tokenize import word_tokenize

data = "White House organizing program to slash development time for coronavirus vaccine by as much as eight months"

#file =  open('text.txt', 'r') 
#data = file.read().replace('\n', '')

potter_stem = PorterStemmer() #stemming

for i in word_tokenize(data):
    print(potter_stem.stem(i))
