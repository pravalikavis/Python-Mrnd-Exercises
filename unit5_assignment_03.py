__author__ = 'Kalyan'

notes = '''
Now we move on to writing both the function and the tests yourself.

In this assignment you have to write both the tests and the code. We will verify your code against our own tests
after you submit.
'''

# fill up this routine to test if the 2 given words given are anagrams of each other. http://en.wikipedia.org/wiki/Anagram
# your code should handle
#  - None inputs
#  - Case  (e.g Tip and Pit are anagrams)
def are_anagrams(first, second):
    if type(first).__name__ == 'NoneType' or type(second).__name__ == 'NoneType':
        return False
    if type(first).__name__!='str' or type(second).__name__!='str':
        raise TypeError
    if len(first)==len(second):
        f=set(first)
        s=set(second)
        if f==s:
            second=list(second)
            for a in first:
                s=0
                for b in range(len(second)):
                    if a==second[b]:
                        s=1
                        second[b]='0'
                        break
                if s!=1:
                    return False
            return True
    return False


# write your own exhaustive tests based on the spec given
def test_are_anagrams_student():
    assert True == are_anagrams("pit", "tip") #sample test.
    assert False == are_anagrams("pi", "tip")
    try:
        are_anagrams(124,241)
    except TypeError as te:
        print(te)

    assert False==   are_anagrams(None,None)

    assert False==are_anagrams("aaaae","aeeee")


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_are_anagrams_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_are_anagrams(are_anagrams)
