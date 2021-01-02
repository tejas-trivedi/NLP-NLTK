# Objective: To find the similarity between two sentences/documents

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords,wordnet
from nltk.stem import WordNetLemmatizer
from itertools import product
import numpy


str1 = " White House organizing program to slash development time for coronavirus vaccine by as much as eight months"
str2 = "White House risks backlash with coronavirus optimism if cases flare up again."

# Defining stopwords for English language
stop_words = set(stopwords.words("english"))

filtered_sentence1 = []
filtered_sentence2 = []
lemma_sentence1 = []
lemma_sentence2 = []
sims = []
temp1 = []
temp2 = []
similar = []
final = []
same_sent1 = []
same_sent2 = []


# Defining WordNet Lemmatizer
lemmatizer  =  WordNetLemmatizer()

# Tokenizing and removing the Stopwords
for words1 in word_tokenize(str1):
    if words1 not in stop_words:
        if words1.isalnum():
            filtered_sentence1.append(words1)

# Root words
for i in filtered_sentence1:
    lemma_sentence1.append(lemmatizer.lemmatize(i))
    

# Tokenizing and removing the Stopwords
for words2 in word_tokenize(str2):
    if words2 not in stop_words:
        if words2.isalnum():
            filtered_sentence2.append(words2)

# Root words
for i in filtered_sentence2:
    lemma_sentence2.append(lemmatizer.lemmatize(i))
    

# Removing same words from token
for word1 in lemma_sentence1:
    for word2 in lemma_sentence2:
        if word1 == word2:
            same_sent1.append(word1)
            same_sent2.append(word2)
            
if same_sent1 != []:
   for word1 in same_sent1:
    lemma_sentence1.remove(word1)
if same_sent2 != []:
   for word2 in same_sent2:
    lemma_sentence2.remove(word2)
            
print(lemma_sentence1)
print(lemma_sentence2)


# Similarity index for each word
for word1 in lemma_sentence1:
    similar =[]
    for word2 in lemma_sentence2:
        sims = []
        syns1 = wordnet.synsets(word1)
        syns2 = wordnet.synsets(word2)
        for sense1, sense2 in product(syns1, syns2):
            d = wordnet.wup_similarity(sense1, sense2)
            if d != None:
                sims.append(d)
    
        if sims != []:        
           max_sim = max(sims)
           similar.append(max_sim)
             
    if similar != []:
        max_final = max(similar)
        final.append(max_final)


# Final Output
similarity_index = numpy.mean(final)
similarity_index = round(similarity_index , 2)
print("Sentence 1: ",str1)
print("Sentence 2: ",str2)
print("Similarity index value : ", similarity_index)

if similarity_index>0.8:
    print("Similar")
elif similarity_index>=0.6:
    print("Somewhat Similar")
else:
    print("Not Similar")
