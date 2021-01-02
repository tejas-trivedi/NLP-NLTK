# Chinking is a lot like Chunking except that it removes unwanted
# chunks from the chunks obtained through Chunking.

import nltk
from nltk.tokenize import sent_tokenize

file =  open('text.txt', 'r') 
data = file.read().replace('\n', '')

tokenized = sent_tokenize(data)

def process_content():
    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            chunkGram="""Chunk: {<.*>+}
                        }<VB.?|IN|DT>+{"""
            chunkParser=nltk.RegexpParser(chunkGram)
            chunked=chunkParser.parse(tagged)
            print(chunked)
            chunked.draw()
        
    except Exception as e:
        print(str(e))

process_content()
