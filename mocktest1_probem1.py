__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given 2 strings str1 and str2, find out the minimum number of right rotations str1 needs to undergo
to create str2. If is not possible, return -1

Notes:
1. Assume inputs are either None or valid strings
2. Write plain brute force code.
3. result should be -1 if not possible
4. If it is possible then give the 'minimum rotations' required.
5. No need for type checking.
'''

def get_right_rotations(str1, str2):
    if str1==None:
        return -1
    if(str1==str2):
        return 0
    i=len(str1)
    l=0
    for j in range(1,i):
        l+=1
        str1=str1[-j]+str1
        if(str1[:-j]==str2):
         return l
    return -1



# basic test given, write more tests to ensure correctness.
def test_get_right_rotations():
    assert 1 == get_right_rotations("abcd", "dabc")
    assert -1== get_right_rotations("abcd", None)
    assert 2 == get_right_rotations("abcd", "cdab")
    assert -1 == get_right_rotations("abcd", "")