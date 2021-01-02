# Chunking is a process of extracting phrases from unstructured text, which means analyzing a sentence to identify the constituents
# Chunking helps us identify regarding what object we are making the opinion.

import nltk
from nltk.tokenize import PunktSentenceTokenizer

file =  open('text.txt', 'r') 
data = file.read().replace('\n', '')

custom_sent_tokenizer= PunktSentenceTokenizer(data)
tokenized = custom_sent_tokenizer.tokenize(data)

def process_content():
    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            #.?and * are regexps. 
            chunkGram="""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}"""
            chunkParser=nltk.RegexpParser(chunkGram)
            chunked=chunkParser.parse(tagged)
            print(chunked)
            chunked.draw()
    except Exception as e:
        print(str(e))

process_content()
