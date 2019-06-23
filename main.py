from nltk.corpus import words
import json
from nltk.corpus import abc
from collections import Counter
print(abc.subdir)
print(len(words.words()))

DICTIONARY_NLTK = words.words()


if 'stupid' in DICTIONARY_NLTK:
    print('Heloooo')

with open('BrowserHistory.json','r') as f:
    search_dict = json.load(f)

word_list = list()
for words in search_dict:
    word_list= word_list + [ word.lower() for word in words['title'].split(' ')]

WORDS = Counter(word_list)

print(WORDS)