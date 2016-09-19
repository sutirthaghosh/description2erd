import nltk
import re
import sys
import nltk.data
sentence_tokens = []
noun = {}
verb = {}

entities = {}
relations ={}

f = open('text', 'r')
input_string = f.read()

sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')

sentences = sentence_detector.tokenize(input_string.strip())
print(sentences)
# start getting pure words from sentence a 2D array with each row containing words in a sentence
for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    words = [w.lower() for w in tokens if w.isalnum()]
    sentence_tokens.append(words)
# POS tagging the words in sentence_tokens
for words in sentence_tokens:
    print(nltk.pos_tag(words))

print(sentence_tokens)
