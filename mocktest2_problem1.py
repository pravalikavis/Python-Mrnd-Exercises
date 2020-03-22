max_marks = 20

problem_notes = '''
Given a sentence in which words are separated by spaces.

Re-arrange it so that words are reordered according to the following criteria.
 - longer words come before shorter words
 - if two words have same length, the one with smaller vowel occurance count comes first (feeel counts as 3 vowel occurances)
 - if even that is same, then order them lexicographically (case insensitive). For e.g. a comes before b

Constraints:
- Only allowed characters are a-zA-Z in the words
- raise a ValueError if the sentence contains any characters beyond the above
- raise a TypeError if input is not a string
- The result should preserve the words as is without changing case etc. but the sentence should be sorted so that
longer words precede shorter words. In case of tie, the word with fewer vowels comes first, if there is a tie even there,
preserve the original order.
- If there are multiple spaces, merge them into a single space in the result.
- If there is any leading or trailing space, remove it from the result.


Note: 
1. use the features of python to solve this problem, DON'T WRITE YOUR OWN SORT ROUTINE!
2. You can write additional routines as you see fit.
'''
import re
vowels=['a','e','i','o','u']
def vow_count(s):
    count=0
    for a in s:
        if a.lower() in vowels:
            count=count+1
    return count
from itertools import groupby
import string
alpha=list(string.ascii_lowercase)
alpha.append(' ')
def transform(sentence):
    if type(sentence).__name__!='str':
        raise TypeError
    for a in sentence:
        if a.lower() not in alpha:
            raise ValueError
    inp_test = re.sub("[^\w|,|/.]", " ", sentence).split()

    inp_test=     sorted(inp_test,key=lambda x:(len(x)),reverse=True)
    s=''
    for key,group in groupby(inp_test,lambda x:len(x)):

        for a in  sorted(list(group),key=lambda x:(vow_count(x),x.lower())):
            s=s+a+' '


    return s[:-1]

def test_transform():
    assert "elephant walking runway on" == transform("walking elephant on runway")