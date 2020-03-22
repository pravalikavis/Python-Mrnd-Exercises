__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""
import re
import sys
from placeholders import *
vowel=['a','e','i','o','u']
def add_ay(wordList ,wordList1,a):
    if wordList[a][-1] == ',' or wordList[a][-1] == '.':
        wordList1[a] = wordList1[a][:-1] + 'ay' + wordList1[a][-1:]
    else:
        wordList1[a] = wordList1[a] + 'ay'


def add_capital(wordList1,a,capital_pos):
    wordList1[a] = wordList1[a][:capital_pos] + wordList1[a][capital_pos].upper() + wordList1[a][capital_pos + 1:]


def transitions(wordList,wordList1):
    for a in range(len(wordList)):
        capital=0
        capital_pos=0
        for b in range(len(wordList[a])):

            if wordList[a][b] in vowel:

                break
            else:
                if wordList[a][b].isupper()==True:
                    capital=1
                    capital_pos=b
                if wordList[a][-1] == ',' or wordList[a][-1] == '.':
                    wordList1[a] = wordList1[a][1:-1] + wordList1[a][0].lower() + wordList1[a][-1:]
                else:
                    wordList1[a] = wordList1[a][1:] + wordList1[a][0].lower()
        add_ay(wordList, wordList1, a)
        if capital==1:
            add_capital(wordList1,a,capital_pos)


def pig_latin(inp_s):

    wordList = re.sub("[^\w|,|/.]", " ", inp_s).split()
    wordList1 = wordList[:]

    transitions(wordList,wordList1)

    return wordList1


def test_pig_latin_1(inp):
        inp_test= re.sub("[^\w|,|/.]", " ", inp).split()
        inp_len=[len(x) for x in inp_test]
        words=pig_latin(inp)
        words_len=[len(x) for x in words]
        assert inp_len<words_len
        for a in words:
            if a[-3:-1] =='ay' or a[-2:]=='ay':
                assert True
            else:
                assert False

if __name__ == "__main__":
    inp=input("enter a string:")
    test_pig_latin_1(inp)

    print(pig_latin(inp))
    #sys.exit(main())