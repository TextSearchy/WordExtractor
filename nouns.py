#!/usr/bin/python
from textblob import TextBlob
textinput = """Insert random text here to get the noun phrases"""
randomText = TextBlob("Same random text here will give the type/attribute of every word")
print(randomText.tags)		##Gives attribute of every word: Noun, Verb...
blob = TextBlob(textinput)
print(blob.noun_phrases)	##Gives only the noun phrases


##pip install -U textblob
##python -m textblob.download_corpora
##pip install -U nltk => Not needed now, will be needed later, bery bery usephul.
