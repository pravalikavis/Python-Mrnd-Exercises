__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Palindrome is a word which spells the same from both ends.

Create the smallest palindrome from a given word by appending characters to its end.

Examples:
- Malayalam -> Malayalam
- Malayal -> Malayalam (we want smallest palindrome)


Notes:
1. Don't change the letters of the initial word, only add new small letters
2. The palindrome is case-insensitive (ie) Tat is a valid palindrome
3. Only letters are allowed, any other characters should raise a ValueError
4. Non strings should raise a TypeError
5. Empty string is considered as a palindrome.
'''
import string
s=string.ascii_lowercase
s=s+string.ascii_uppercase
def smallest_palindrome(word):
    if type(word).__name__!='str':
        raise TypeError
    for a in word:
        if a not in s:
            raise ValueError
    i=len(word)
    for j in range(len(word)):
        if(word.lower()==word[::-1].lower()):
            return word
        if(word[j]!=word[len(word)-1-j]):
            word=word[:len(word)-j]+word[j]+word[len(word)-j:]
        i-=1





# write your own tests
def test_smallest_palindrome():
    assert "Malayalam"==smallest_palindrome("Malayalam")
    assert "malAyAlam" == smallest_palindrome("malAyA")
    try:
        smallest_palindrome(None)
    except TypeError:
        pass
    try:
        smallest_palindrome("1ssxsx")
    except ValueError:
        pass