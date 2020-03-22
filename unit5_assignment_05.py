__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
def prune_either_or(sentence):
    if type(sentence).__name__!='str':
        raise TypeError
    l=sentence.find(" either")
    if(l==-1):
        return sentence
    s=sentence.replace(" either","")
    l=s.find(" or ")
    if(l==-1):
        return sentence
    s=s[:l]
    while(s.find("  ")!=-1):
     s=s.replace("  "," ")
    if s[-1]==" ":
        return s[:-1]
    return s
def test_prune_either_or_student():
    assert "we could go to a movie"==prune_either_or("we could either go to a movie or a hotel")
    assert "we could go to a movie" == prune_either_or("we  could either go to a movie or        a hotel")
    assert "we could go to a movie or a hotel" == prune_either_or("we could go to a movie or a hotel")
    assert "we could either go to a movie  a hotel" == prune_either_or("we could either go to a movie  a hotel")
    try :
        prune_either_or(None)
    except TypeError as te:
        print(te)
    try :
        prune_either_or(123)
    except TypeError as te:
        print(te)
# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
