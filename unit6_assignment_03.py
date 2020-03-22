__author__ = 'Kalyan'

notes = '''
 This problem will require you to put together many things you have learnt
 in earlier units to solve a problem.

 In particular you will use functions, nested functions, file i/o, functions, lists, dicts, iterators, generators,
 comprehensions,  sorting etc.

 Read the constraints carefully and account for all of them. This is slightly
 bigger than problems you have seen so far, so decompose it to smaller problems
 and solve and test them independently and finally put them together.

 Write subroutines which solve specific subproblems and test them independently instead of writing one big
 mammoth function.

 Do not modify the input file, the same constraints for processing input hold as for unit6_assignment_02
'''

problem = '''
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 source - file containing words, one word per line, some words may be capitalized, some may not be.
 - read words from the source file.
 - group them into anagrams. how?
 - sort each group in a case insensitive manner
 - sort these groups by length (desc) and in case of tie, the first word of each group
 - write out these groups into destination
'''

import unit6utils
import string



def est1(li):
    r=[]
    for a in range(len(li)):
        s=[]
        for b in range(a+1,len(li)):
            if li[b]!="":
                if len(li[a])==len(li[b]):
                 x=[z.lower() for z in li[a]]
                 y=[z.lower() for z in li[b]]
                 x.sort()
                 y.sort()
                 if x==y:
                    s.append(li[b])

                    li[b]=""
        if s!=[]:
            s.append(li[a])
            li[a]=""
            s.sort(key=lambda x:len(x))
            r.append(s)
    return r





def anagram_sort(source, destination):
    f = open(source, "r")
    l = [x if '#' not in x else x[:x.index('#')].strip() for x in f.readlines() if x[0] != '#' and x != '\n']

    l = [x if x[-1] != '\n' else x[:-1] for x in l if x != '']
    l1=est1(l)
    l1 = [sorted(x, key=lambda x: x.lower()) for x in l1]
    l1.sort(key=lambda x: (x[0].lower(), len(x)), reverse=True)


    l1.reverse()
    l.sort(key=lambda x: (x.lower(), len(x)))
    with open(destination,"w") as f1:
        for a in l1:
            for b in a:
                f1.write(b)
                f1.write('\n')
        for a in l:
            if a!='':
                f1.write(a)
                f1.write('\n')
    f.close()
    f1.close()

def test_anagram_sort():
    source = unit6utils.get_input_file("unit6_testinput_03.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_03.txt")
    destination = unit6utils.get_temp_file("unit6_output_03.txt")
    anagram_sort(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
