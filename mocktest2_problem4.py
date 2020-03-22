__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
You're given a text file containing names of movie actors and films they've acted in - delimited
by : after actor and movies are separated by commas as described below. movie names may contain : and space
too but not a comma.

Format:
{actor name}: {movie name 1}, {movie name 2}, {movie name 3}

Input:
File containing movies info, a number 'n' which represents the number of lines from top of file and a list 
of movies that I like.  n is used to simulate various files instead of having different movies files for testing.

Output:
The top k actors that I might like based on the movies given. The actors are sorted by the number of movies 
they acted in (descending). In case of a tie, sort by name (insensitive)

Example:
I like movies m1, m2, m3 and the actors who acted in them (in the first N lines) are as follows
m1 : a1, a3, a5 
m2 : a2, a3
m3:  a2, a3, a6

Then top 2 actors that I might like are a3 and a2.

Notes:
1. No special type checking required. raise ValueError if n < 0. 
2. You must work as if the file has only n lines.
3. See if you can decompose this problem into meaningful subroutines.
4. If a movie that is given do not exist in the top N lines, then ignore that movie (as if no one acted in it)
5. The movies must be treated in a case insensitive manner (ie) Inception and inception refer to the same movie. 
6. The actors returned must be in the same case as given in the input file (Tom Hardy and not tom hardy).   

UPLOAD THE movies.txt file into your drive folder as well ** Do not modify the movies.txt file! **

'''

import inspect
import os


# returns the top k actors sorted by the specified criteria.
# It is as if the file has only first n lines.
# Important: Use the helper routine given (open_input_file) to open the file to open the file which should
# be in same directory as this file.
'''
def get_favorite_actors(input_file, n, movies, k):
    if n<0:
        raise ValueError

    dic={}
    res=[]
    a1=-1
    b1=-1
    f=open_input_file(input_file)
    for a in range(n):
        l=f.readline()
        if l.split(':',1)[0] not in dic:
            dic.update({l.split(':',1)[0]:len(l.split(','))})
        else:
            dic[l.split(':',1)[0]]=dic[l.split(':',1)[0]]+len(l.split(','))

    for a in dic:
            s=[]
            a1=a1+1
            for b in dic:
                b1=b1+1
                if b1<=a1:
                    continue
                if dic[a]==dic[b] and dic[a]!=0:

                    s.append(b)
                    dic[b]=0

            if dic[a] != 0:
                s.append(a)
                s.append(dic[a])
                res.append(s)
                dic[a] = 0

            b1 = -1
    res=sorted(res,key=lambda x:x[-1])
    res.reverse()
    result=[]
    for x in res:
        inte=[]
        for y in range(len(x)-1):
            inte.append(x[y])
        inte.sort(key=lambda x:x.lower())
        for y in inte:
            result.append(y)


    return result[:k]
'''
import operator
from itertools import groupby
def get_favorite_actors(input_file, n, movies, k):

    d={}
    for i in movies:
        b=[]
        f = open_input_file(input_file, "r")
        for j in range(n):
            a=f.readline()
            if i in a or i.lower() in a or i.strip() in a or i.strip().lower() in a:
                if d.__contains__(a.split(':')[0])==False:
                    d[a.split(':')[0]]=1
                else:
                    d[a.split(':')[0]] = d[a.split(':')[0]]+1
    res=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
    res_r=[]
    for key,group in groupby(res,key=lambda x:x[1]):
        for a in sorted(list(group)):
            res_r.append(a)
    return [x[0] for x in res_r][:k]









def test_get_favorite_actors():
    assert ['Leonardo Di Caprio', 'Tom Hardy'] == get_favorite_actors("movies.txt", 4, ["Inception"], 2)


def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)


def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir


