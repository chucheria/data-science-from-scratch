# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:39:41 2016

@author: beatriz.hernandez
"""

# The Zen of Python

import this


# Whitespace formatting

for i in [1, 2, 3, 4, 5]:
    print i                             # first line in "for i" block
    for j in [1, 2, 3, 4, 5]:
        print j                         # first line in "for j" block
        print i + j                     # last line in "for j" block
    print i                             # last line in "for i" block
print 'done looping'

# whitespace is ignored inside patentheses and brackets
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
easier_to_read_list_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]


# Modules

import re
my_regex = re.compile('[0-9]+', re.I)           # import the module itself

# import the module with an alias
import re as regex
my_regex = regex.compile('[0-9]+', re.I)

import matplotlib.pyplot as plt

# import specific values from a module
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()


# Arithmetic

from __future__ import division
5 / 2           # 2.5
5 // 2          # 2


# Functions
def double(x):
    """ this function multiplies its input by 2 """
    return x * 2


def apply_to_one(f):
    """
    calls the function f with 1 as its argument
    functions are first-class, we can assign them to variables
    and pass them into functions
    """
    return f(1)


my_double = double              # refers to the previously defined function
x = apply_to_one(my_double)     # equals 2

y = apply_to_one(lambda x: x + 4)   # equals 5


def my_print(message='my default message'):
    """ functions parameters can be given default arguments """
    print message

my_print('Hello')               # prints Hello
my_print()                      # prints my default message

def substract(a=0, b=0):
    return a - b

substract(10, 5)                # 5
substract(0, 5)                 # -5
substract(b=5)                  # -5


# Strings

single_quoted_string = 'data science'
double_quoted_string = "data science"

tab_string = '\t'               # represents the tab character
len(tab_string)                 # 1

not_tab_string = r'\t'          # represents the characters \ and t
len(not_tab_string)             # 2

multi_line_string = ''' This is the first line.
                    This is the second line.'''


# Exceptions

try:
    print 0 / 0
except ZeroDivisionError:
    print 'cannot divide by zero'


# Lists

integer_list = [1, 2, 3]
heterogeneous_list = ['string', 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]

list_length = len(integer_list)             # 3
list_sum = sum(integer_list)                # 6

x = range(10)               # [0, 1, ..., 9]
first_eleement = x[0]       # 0
last_element = x[-1]        # 9
x[0] = -1                   # [-1, 1, ..., 9]

first_three = x[:3]         # [-1, 1, 2]
three_to_end = x[3:]        # [3, 4, ..., 9]
one_to_four = x[1:5]        # [1, 2, 3, 4]
last_three = x[-3:]         # [7, 8, 9]
copy_of_x = x[:]            # copy of x

1 in [1, 2, 3]              # True
0 in [1, 2, 3]              # False

x = [1, 2, 3]
x.extend([4, 5, 6])         # x is now [1, 2, 3, 4, 5, 6]
y = x + [7, 8, 9]           # y is now [1, 2, 3, 4, 5, 6, 7, 8, 9]
x.append(0)                 # x is now [1, 2, 3, 4, 5, 6, 0]

x, y = [1, 2]               # x = 1, y = 2
_, y = [1, 2]               # y = 2 and the first element is irrelevant


# Tuples

my_tuple = (1, 2)
other_tuple = 3, 4

try:
    my_tuple[1] = 3
except TypeError:
    print 'cannot modify a tuple'


def sum_and_product(x, y):
    """ tuples are a convenient way to return multiple values from functions"""
    return (x + y), (x * y)


sp = sum_and_product(2, 3)      # (5, 6)
s, p = sum_and_product(5, 10)   # s = 15, p = 50

x, y = 1, 2
x, y = y, x                     # swap variables


# Dictionaries

empty_dict = {}                     # pythonic
grades = {'Joel': 80, 'Tim': 95}  # dictionary
joels_grade = grades['Joel']        # 80
try:                                # you'll get a KeyError if ask for a key
    kates_grade = grades['Kate']    # that's not in the dictionary
except KeyError:
    print 'no grade for Kate'

joel_has_grade = 'Joel' in grades   # True
kate_has_grade = 'Kate' in grades   # False

# if key is not in dictionary returns 0 which is default value
joels_grade = grades.get('Joel', 0)
kates_grade = grades.get('Kate', 0)     # 0
no_ones_grade = grades.get('No One')    # if default not specified then is None

grades['Tim'] = 99                  # replaces old value
grades['Kate'] = 100                # add a third entry
num_students = len(grades)          # 3

tweet = {
    'user': 'chucheria',
    'text': 'holi',
    'retweet_count': 100,
    'hashtags': ['greetings', 'holi']
}                                   # representing structured data

tweet_keys = tweet.keys()           # list of keys
tweet_values = tweet.values()

'user' in tweet                     # uses a fast dict in
'chucheria' in tweet_values

# defaultdict

word_counts = {}
for word in document:
    if word in word_counts:
        # increment word count if it's already in the dictionary
        word_counts[word] += 1
    else:
        word_counts[word] = 1       # add word to the dictionary if it's not

word_counts = {}
for word in document:
    try:
        word_counts[word] += 1      # try to look up a missing key
    except KeyError:
        word_counts[word] = 1

word_counts = {}
for word in document:
    precious_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

from collections import defaultdict

word_counts = defaultdict(int)      # defaultdict is like a regular dictionary
# except that when you try to look up a key it
# doesn’t contain, it first adds a value for it
# using a zero-argument function you provided
for word in document:
    word_counts[word] += 1          # when you created it,int() produces 0

dd_list = defaultdict(list)         # list() produces an empty dict
dd_list[2].append(1)                # dd_list = {2: [1]}

dd_dict = defaultdict(dict)          # dict() produces an empty dict
dd_dict['Joel']['City'] = 'Seattle'  # { 'Joel' : { 'City: Seattle' }}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                   # dd_pair = {2: [0, 1]}


# Counter

from collections import Counter
# c is a Counter like { 0 : 2, 1 : 1, 2 : 1}
c = Counter([0, 1, 2, 0])

word_counts = Counter(document)     # to counts words in document

for word, count in word_counts.most_common(10):
    print word, count


# Sets

s = set()
s.add(1)            # s = { 1 }
s.add(2)            # s = { 1, 2 }
s.add(2)            # s = { 1, 2 }

x = len(s)          # x = 2
3 in s              # False

'zip' in words       # checks every element - slow if long list
'zip' in set(words)  # very fast to check

items = [1, 2, 3, 1, 2, 3]
len(items)                      # 6
distinct = len(set(items))      # 3


# Control flow

if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"

parity = "even" if x % 2 == 0 else "odd"        # write a ternary if-then-else!

x = 0
while x < 10:                                   # while loop
    print x, "is less than 10"
    x += 1

for x in range(10):                             # for loop
    print x, "is less than 10"

for x in range(10):
    if x == 3:
        continue                # go immediately to the next iteration
    if x == 5:
        break                   # quit the loop entirely
    print x


# Truthiness

1 < 2               # True
True == False       # False

x = None
print x is None     # True and Pythonic

s = some_function_that_returns_a_string()
if s:
    # if s is a non-empty string then is True
    first_char = s[0]
else:
    first_char = ''

# and returns the second value when the first is "truthy"
first_char = s and s[9]

# if x is a number or possibly None - this returns 0 if "falsy"
safe_x = x or 0
