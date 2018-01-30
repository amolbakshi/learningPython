import nltk
import re
from nltk.tokenize import PunktSentenceTokenizer

isdaData = open("sampleISDA.txt",encoding="utf8").read()
trainedTokenizer = PunktSentenceTokenizer(isdaData)
tokanizedData = trainedTokenizer.tokenize(isdaData)

def processISDA():
    try:
        for i in tokanizedData:
            stripped = i.replace(',','')
            stripped=re.sub(r'[^a-zA-Z0-9]', ' ', stripped)
            words = nltk.word_tokenize(stripped,'english')
            tagged = nltk.pos_tag(words)
            grammar = r"""
              NP:
                {<.*>+}          # Chunk everything
                }<IN|DT|JJ|VBD|RB.?>+{      # Chink sequences of VBD and IN
              """

#            grammar = r"""Chunk:{<.*>+}
#                            }<IN|DT>{"""
            chunkParser = nltk.RegexpParser(grammar)
            chunked = chunkParser.parse(tagged)
            namedEntity = nltk.ne_chunk(tagged)
            print(namedEntity)
    except Exception as e:
        print(e)

processISDA()

