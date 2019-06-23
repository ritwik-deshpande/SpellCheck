
from main import DICTIONARY_NLTK,WORDS




def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in DICTIONARY_NLTK)




def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N

def correction(word):
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word):
    "Generate possible spelling corrections for word."
    possible_words = set()

    for word in known([word]):
        possible_words.add(word)

    for word in known(edits1(word)):
        possible_words.add(word)

    for word in known(edits2(word)):
        possible_words.add(word)

    return possible_words



if __name__ =='__main__':
    print(WORDS)
    print(len(DICTIONARY_NLTK))

    word = 'seerch'


    print(correction(word))