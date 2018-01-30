from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

""" Stop words usage """
line = "This is Amol trying his hands on nltk. Lets see where we reach.This might be pretty darn good."
stopWords = set(stopwords.words("english"))
wordsInLine = word_tokenize(line)
emptyWords = []
for w in wordsInLine:
    if w not in stopWords:
        emptyWords.append(w)

print(emptyWords)
""" Stop words usage """