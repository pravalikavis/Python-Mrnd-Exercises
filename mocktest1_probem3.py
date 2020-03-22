__author__ = 'Kalyan'

max_marks = 35 # 15 marks for encode and 20 for decode

problem_notes ='''
 This problem deals with number conversion into a custom base 5 notation and back.
 In this notation, the vowels a e i o u are used for digits 0 to 4.

 E.g. decimal 10 in this custom base 5 notation is "ia", decimal 5 is "ea" etc.

 Your job is to write encoding and decoding (both) routines to deal with this notation.
'''

# Notes:
# - If number is not a valid int raise TypeError
# - Negative numbers should result in a - prefix to the result similar to how bin works
#  use lower case letters in your result [aeiou].
ref="aeiou"
def to_custom_base5(number):
    if type(number).__name__!='int':
        raise TypeError
    sign=0
    if number<0:
        sign=1
        number=number*-1
    r=[]
    while number>5:
        r.append(number%5)
        number=number/5
    if number>0:
        r.append(int(number))
    r=r[::-1]
    res=""
    for i in r:
        res=res+ref[i]
    if sign==1:
        res='-'+res
    return res

# Notes:
# - if s is not a string, raise TypeError
# - if the encoding is not right or empty string, raise ValueError
# - allow both - and + as prefixes which represent sign.
# - allow trailing and starting spaces (but not once the sign or number starts)
# - allow both capital and small letters.
# - return a int that corresponds to the number.
re={'a':0,'e':1,'i':2,'o':3,'u':4,'+':0,"-":0}
def from_custom_base5(s):
    if type(s).__name__!='str':
        raise TypeError
    if len(s)<1:
        raise ValueError
    c = 0
    c1 = 0
    i=0
    for a in s:

        if i==0 and a!=" ":
         if a.lower() not in re:
            raise ValueError
         else :
             i=1
    sign=0
    i=0

    r=len(s)-1
    for a in s:
        if a=='+' or a=='-':
            if a=='-':
             sign=1
            r=r-1
        elif a==' ':
            r=r-1
        else:
         i=i+re[a.lower()]*(5**r)
         r=r-1
    if sign==1:
        i=i*-1
    return i



# a basic test is given, write your own tests based on constraints.
def test_to_custom_base5():
    assert "ia" == to_custom_base5(10)
    assert "oa" == to_custom_base5(+15)


# a basic test is given, write your own tests based on constraints.
def test_from_custom_base5():
    assert 10 == from_custom_base5("ia")
    assert 15 == from_custom_base5(" Oa")