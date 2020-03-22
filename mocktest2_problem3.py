__author__ = 'Kalyan'

max_marks = 30

problem_notes = '''
For this problem you have to implement a generator which returns all k digit 
numbers whose sum of digits is n. 

Note that you must not generate the entire solution set at one go (ie) the 
result should be generated on demand (when next is called on generator). This means that 
I can call it with large values of n and k like 1000 and 500 and still 
its use of memory must be modest.

Notes:
1. raise TypeError if n and k are not ints.  
2. if n or k are not positive, raise ValueError 
3. the result numbers must be yield'ed in increasing order. 
4. you are free (encouraged :-) ) to define additional sub-routines as you see fit as long as you do not   
   violate the generator semantics given above

Examples:
 for n = 2 and k = 2, the generator must yield 11, 20 in that order
 for n = 4 and k = 2, the generator must yield 13, 22,31,40 in that order
 
Note that numbers starting with 0 are not valid For e.g. 02 is not a valid 2 digit number
'''

#Implement this generator.
def sum(n):
    sum_res=0
    while(n>0):
        sum_res=sum_res+int(n%10)
        n=int(n/10)
    return sum_res



def compute1(l):
    for a in range(1,len(l)+1):
        if l[-(a)]>0:
            l[-(a)]-=1
            for b in range(a+1,len(l)+1):
                if l[-b]<9:
                    l[-b]+=1
                    break
            break
    return l



from functools import *;


def kdigitnums(n, k):
    """
    This is a generator returns all k digit numbers whose sum is n. The numbers are yielded in
    increasing order
    """
    if type(n).__name__!='int' or type(k).__name__!='int':
        raise TypeError
    if n<0 or k<0:
        raise ValueError
    x=n
    a=1
    a=a*(10**(k-1))
    b=a*10
    l=[  int( int(  int(a/(10**x)) )%10 )        for x in range(k)]
    l.reverse()
    x=x-1
    if n>b:
        raise StopIteration
    try:
        if (x <= 9):
            l[-1] =l[-1]+ x
        else:
            a = 1
            while (x > 9):
                l[-a] =l[-a]+  9
                x = x - 9
            else:
                l[-a] =l[-a]+ x
    except IndexError :
        raise StopIteration
    res=a
    while(res<b):
        res=0
        for x in l:
            res=res*10+x
        if reduce(lambda x,y:x+y,l) !=n:
            raise StopIteration


        yield res
        l=compute1(l)












# write more tests
def test_kdigitnums():
    assert [1000000009, 1000000018, 1000000027, 1000000036, 1000000045, 1000000054, 1000000063, 1000000072, 1000000081, 1000000090, 1000000180, 1000000270, 1000000360, 1000000450, 1000000540, 1000000630, 1000000720, 1000000810, 1000000900, 1000001800, 1000002700, 1000003600, 1000004500, 1000005400, 1000006300, 1000007200, 1000008100, 1000009000, 1000018000, 1000027000, 1000036000, 1000045000, 1000054000, 1000063000, 1000072000, 1000081000, 1000090000, 1000180000, 1000270000, 1000360000, 1000450000, 1000540000, 1000630000, 1000720000, 1000810000, 1000900000, 1001800000, 1002700000, 1003600000, 1004500000, 1005400000, 1006300000, 1007200000, 1008100000, 1009000000, 1018000000, 1027000000, 1036000000, 1045000000, 1054000000, 1063000000, 1072000000, 1081000000, 1090000000, 1180000000, 1270000000, 1360000000, 1450000000, 1540000000, 1630000000, 1720000000, 1810000000, 1900000000, 2800000000, 3700000000, 4600000000, 5500000000, 6400000000, 7300000000, 8200000000, 9100000000] == list(kdigitnums(10,10))

