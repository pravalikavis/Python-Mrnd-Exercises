__author__ = 'Kalyan'

max_marks = 30

problem_notes = '''
This problem is the reverse of problem3. Given the jumbled text created 
according to the rules given in problem 3 and number of steps, create the original text.

Notes:
1. Raise ValueError if n <= 0
2. Raise TypeError if text is not a str
3. Do not search for mathematical patterns, solve this programatically
'''


def unjumble(jumbled_text, n):
    if n <= 0:
        raise ValueError
    if type(jumbled_text).__name__ != 'str':
        raise TypeError
    cal = [[x, 0] for x in range(1, n + 1)]
    o = 0
    c = n
    text = jumbled_text
    while text != "":
        cal[c - 1][1] += 1
        text = text[c:]
        if o == 0:
            c = c - 1
            if c == 0:
                c = 0
                o = 1
        if o == 1:
            if c == n:
                o = 0
                continue
            c = c + 1
    c = 1
    l = []
    o = 1
    text = jumbled_text
    while text != "":
        a = cal[c - 1][1]
        b = ""
        while a > 0:
            b = b + text[:c]

            text = text[c:]
            a = a - 1
        l.append([b, c])
        if o == 0:
            c = c - 1
            if c == 0:
                c = 0
                o = 1
        if o == 1:
            if c == n:
                o = 0
                continue
            c = c + 1
    a = len(l) - 1
    c = a
    res = ""
    o = 0
    while True:
        if a < 0 or a >= len(cal):
            break
        b = cal[a][1]
        if b == 0:
            cal.pop(a)

        res = res + l[a][0][:a + 1]
        l[a][0] = l[a][0][a + 1:]
        b = b - 1
        cal[a][1] -= 1
        if o == 0:
            a = a - 1
        if a == -1:
            o = 1
        if o == 1:
            a = a + 1
            if a == len(l):
                o = 0
                a = a - 1
    return res


def test_unjumble():
    assert "Ashokan" == unjumble("hoAskan", 2)

