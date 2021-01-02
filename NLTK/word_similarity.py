from nltk.corpus import wordnet
from itertools import product

sims = []

list1 = ['India']
list2 = ['Tiger']
list = []

print("word1 : ", list1)
print("word2 : ", list2)

for word1,word2 in product(list1,list2):

        syns1 = wordnet.synsets(word1)
        syns2 = wordnet.synsets(word2)

        for sense1, sense2 in product(syns1, syns2):
            d = wordnet.wup_similarity(sense1, sense2)
            if d != None:
                sims.append(d)

print("Similarity index :",max(sims))
        
