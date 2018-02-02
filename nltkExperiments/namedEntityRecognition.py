import nltk
import re
from nltk.tokenize import PunktSentenceTokenizer

trainingData = open("sampleISDA.txt",encoding="utf8").read()
isdaData = open("sampleISDA2.txt",encoding="utf8").read()
trainedTokenizer = PunktSentenceTokenizer(trainingData)
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
            #chunkParser = nltk.RegexpParser(grammar)
            #chunked = chunkParser.parse(tagged)
            namedEntity = nltk.ne_chunk(tagged)
            for w in namedEntity:
                if hasattr(w, '_label') and w._label == 'ORGANIZATION':
                    print(w[0][0])
            #print(namedEntity)
    except Exception as e:
        print(e)

processISDA()

