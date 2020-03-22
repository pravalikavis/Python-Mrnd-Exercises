__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys
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


if __name__ == "__main__":
    inp=input("enter a file name")

    anagram_sort(inp,"results.txt")
    pass
    #sys.exit(main())