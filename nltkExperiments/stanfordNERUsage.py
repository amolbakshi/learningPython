from nltk.tag import StanfordNERTagger
import nltk
import re
from nltk.tokenize import PunktSentenceTokenizer
import os;
from nltk.chunk import conlltags2tree
from nltk.tree import Tree
from nltk import pos_tag

os.environ["JAVA_HOME"] = "C:\Program Files\Java\jre1.8.0_161"

st = StanfordNERTagger(
    'C:\\Users\\amolm\\Downloads\\stanford-ner-2017-06-09\\classifiers\\english.all.3class.distsim.crf.ser.gz',
    'C:\\Users\\amolm\\Downloads\\stanford-ner-2017-06-09\\stanford-ner-3.8.0.jar', encoding='utf-8')

trainingData = open("sampleISDA.txt", encoding="utf8").read()
isdaData = open("sampleISDA2.txt", encoding="utf8").read()
trainedTokenizer = PunktSentenceTokenizer(trainingData)
tokanizedData = trainedTokenizer.tokenize(isdaData)


def bio_tagger(ne_tagged):
    bio_tagged = []
    prev_tag = "O"
    for token, tag in ne_tagged:
        if tag == "O":  # O
            bio_tagged.append((token, tag))
            prev_tag = tag
            continue
        if tag != "O" and prev_tag == "O":  # Begin NE
            bio_tagged.append((token, "B-" + tag))
            prev_tag = tag
        elif prev_tag != "O" and prev_tag == tag:  # Inside NE
            bio_tagged.append((token, "I-" + tag))
            prev_tag = tag
        elif prev_tag != "O" and prev_tag != tag:  # Adjacent NE
            bio_tagged.append((token, "B-" + tag))
            prev_tag = tag
    return bio_tagged


def stanford_tree(bio_tagged):
    tokens, ne_tags = zip(*bio_tagged)
    pos_tags = [pos for token, pos in pos_tag(tokens)]

    conlltags = [(token, pos, ne) for token, pos, ne in zip(tokens, pos_tags, ne_tags)]
    ne_tree = conlltags2tree(conlltags)
    return ne_tree


def structure_ne(ne_tree):
    ne = []
    for subtree in ne_tree:
        if type(subtree) == Tree:  # If subtree is a noun chunk, i.e. NE != "O"
            ne_label = subtree.label()
            ne_string = " ".join([token for token, pos in subtree.leaves()])
            ne.append((ne_string, ne_label))
    return ne


def returntagged():
    stripped = isdaData.replace(',', '')
    stripped = re.sub(r'[^a-zA-Z0-9]', ' ', stripped)
    words = nltk.word_tokenize(stripped, 'english')
    classified_text = st.tag(words)
    return classified_text


print(structure_ne(stanford_tree(bio_tagger(returntagged()))))


def processISDA():
    try:
        for i in tokanizedData:
            stripped = i.replace(',', '')
            stripped = re.sub(r'[^a-zA-Z0-9]', ' ', stripped)
            words = nltk.word_tokenize(stripped, 'english')
            classified_text = st.tag(words)
            for w in classified_text:
                if w[1] == 'ORGANIZATION':
                    print(w)
                    # print(classified_text)
    except Exception as e:
        print(e)
