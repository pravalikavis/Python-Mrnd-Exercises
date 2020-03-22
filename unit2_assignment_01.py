__author__ = 'Kalyan'

notes = '''
1. Read instructions for each function carefully.
2. Feel free to create new functions if needed. Give good names!
3. Use builtins and datatypes that we have seen so far.
4. If something about the function spec is not clear, use the corresponding test
   for clarification.
5. Many python builtin functions allow you to pass functions to customize their behavior. This makes it very productive
   to get things done in python.
'''

# Given a list of age, height of various people [(name, years, cms), .... ]. Sort them in decreasing by age and
# increasing by height.
# NOTE: define a function and pass it to the builtin sort function (key) to get this done, don't do your own sort.
# Do the sort in-place (ie) don't create new lists.

def takeSecond(elem):
    return elem[1]
def takethird(elem):
    return elem[2]

def custom_sort(input):

    if input != None:
        if len(input) > 0 :
         input.sort(key=takeSecond,reverse=True)
         for i in range(len(input)):
             for j in range(i + 1, len(input)):
                 if input[i][1]==input[j][1]:

                     input[i:j+1]=sorted(input[i:j+1],key=takethird)






def single_custom_sort_test(input, expected):
    custom_sort(input) # sorts in place
    assert input == expected

def test_custom_sort():
    # boundary cases
    single_custom_sort_test(None, None)
    single_custom_sort_test([], [])

    # no collisions
    single_custom_sort_test(
        [("Ram", 25, 160), ("Shyam", 30, 162), ("Sita", 15, 130)],
        [("Shyam", 30, 162), ("Ram", 25, 160), ("Sita", 15, 130)])

    # collisions in age
    single_custom_sort_test(
        [("Ram", 25, 165), ("Shyam", 30, 162), ("Ravi", 25, 160), ("Gita", 30, 140)],
        [("Gita", 30, 140), ("Shyam", 30, 162), ("Ravi", 25, 160), ("Ram", 25, 165)])

    # collisions in age and height, then initial order is maintained in stable sorts.
    single_custom_sort_test(
        [("Ram", 25, 165), ("Shyam", 30, 140), ("Ravi", 25, 165), ("Gita", 30, 140)],
        [("Shyam", 30, 140), ("Gita", 30, 140), ("Ram", 25, 165), ("Ravi", 25, 165)])


VOWELS = set("aeiou")
def find(str):
    c=0
    for a in str:
        if a in VOWELS:
            c=c+1
    return c

# returns the word with the maximum number of vowels, in case of tie return
# the word which occurs first. Use the builtin max function and pass a key func to get this done.
def max_vowels(words):
    if words==None:
        return words
    return max(words,key=find,default=None)

def test_max_vowels():
    assert None == max_vowels(None)
    assert None == max_vowels([])

    assert "hello" == max_vowels(["hello", "pot", "gut", "sit"])
    assert "engine" == max_vowels(["engine", "hello", "pot", "gut", "sit"])

    assert "automobile" == max_vowels(["engine", "hello", "pot", "gut", "sit", "automobile"])

    assert "fly" == max_vowels(["fly", "pry", "ply"])


