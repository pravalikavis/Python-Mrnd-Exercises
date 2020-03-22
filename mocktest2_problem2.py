__author__ = 'Kalyan'

max_marks = 25  # encrypt -> 13, decrypt 12

problem_notes = '''
Write encryption and decryption routines according to the given scheme. 

A secret key is used to encrypt a text message in the following manner: 
- key is a string of letters in which each letter represents the right displacement of the source character (a -> 0, z-> 25)
- text -> input text to be sent 

Letters of the input text are mapped to the letters in the key in a round robin manner. For e.g:

For: key = "abcde", text="hi there", the mapping is 
h->a, i -> b, (space is ignored) t ->c, h -> d, e-> e, (go back to starting a here) r -> a, e->b 

now to get the encrypted text, you move h by 0, i by 1, t by 2, h by 3 etc. So you finally get the text "hj vkirf"

The decryption works in the reverse way and returns the original text.

Notes:
- Preserve the casing(lower case remains lower case, Upper case remains Upper case).
- Ignore non-letters and punctuations, i.e., leave them as is in the final result
- For displacement, both small and large letters represent the same displacement. For e.g. b and B both represent 1
- raise TypeError if text and key are not strings.
- raise ValueError if key is empty or has non alphabet characters

Write helper sub routines as required. Make good use of the available datatypes!
'''

# do type checking, non-str should raise TypeException
import string
alpha=dict(zip(list(string.ascii_lowercase),list(range(26))))
num=dict(zip(list(range(26)),list(string.ascii_lowercase)))

def encrypt(text, key):
    if type(text).__name__!='str' or type(text).__name__!='str':
        raise TypeError
    for a in key:
        if a.lower() not in alpha and a !=' ':
            raise ValueError

    res=''
    b=-1
    for a in range(len(text)):
        if text[a].lower()  in alpha:
            b=b+1
            if b>=len(key):
                b=0

            x=alpha.get(key[b].lower())
            y=alpha.get(text[a])
            if x+y <=25:
                res=res+num.get(x+y)
            else:
                res=res+num.get(x+y-26)
        else:
            res=res+" "


    return res

def decrypt(text, key):
    if type(text).__name__!='str' or type(text).__name__!='str':
        raise TypeError
    for a in key:
        if a.lower() not in alpha and a !=' ':
            raise ValueError

    res=''
    b=-1
    for a in range(len(text)):
        if (alpha.get(text[a])):
            b=b+1
            if b>=len(key):
                b=0

            x=alpha.get(key[b].lower())
            y=alpha.get(text[a])
            if y-x>=0:
                res=res+num.get(y-x)
            else:
                res = res + num.get(y - x+26)
        else:
            res=res+" "


    return res

#def test_encrypt():
   # assert "hj vkirf" == encrypt('mysecretmessage', 'secret')


def test_decrypt():
    assert "hi there" == decrypt("ecuvgkwxovwlskg","secret")


