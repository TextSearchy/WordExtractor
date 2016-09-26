#!/usr/bin/python
from textblob import TextBlob
randtext = """The Computer was first invented in the year 1945."""
rndtext = TextBlob("The computer was first invented in the year 1945.")
print(rndtext.tags)		##Gives attribute of every word: Noun, Verb...
blob = TextBlob(randtext)
print(blob.noun_phrases)	##Gives only the noun phrases