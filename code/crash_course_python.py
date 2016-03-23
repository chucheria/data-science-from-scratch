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

long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7)   # whitespace is ignored inside patentheses and brackets

list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
easier_to_read_list_of_lists = [ [1, 2, 3],
                                 [4, 5, 6],
                                 [7, 8, 9] ]            

                                 
# Modules

import re
my_regex = re.compile('[0-9]+', re.I)           # import the module itself

import re as regex
my_regex = regex.compile('[0-9]+', re.I)        # import the module with an alias

import matplotlib.pyplot as plt

from collections import defaultdict, Counter    # import specific values from a module
lookup = defaultdict(int)
my_counter = Counter()


# Arithmetic

from __future__ import division
5 / 2           # 2.5
5 // 2          # 2


# Functions

def double(x):
    ''' this function multiplies its input by 2 '''
    return x * 2

def apply_to_one(f):
    ''' calls the function f with 1 as its argument 
    functions are first-class, we can assign them to variables 
    and pass them into functions '''
    return f(1)

my_double = double              # refers to the previously defined function
x = apply_to_one(my_double)     # equals 2

y = apply_to_one(lambda x: x + 4)   # equals 5

def my_print(message='my default message'):
    ''' functions parameters can be given default arguments'''
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
list_of_lists = [ integer_list, heterogeneous_list, [] ]

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
other_tuple  = 3, 4

try:
    my_tuple[1] = 3
except TypeError:
    print 'cannot modify a tuple'
    
def sum_and_product(x,y):
    ''' tuples are a convenient way to return multiple values from functions '''
    return (x + y),(x * y)

sp = sum_and_product(2, 3)      # (5, 6)
s, p = sum_and_product(5, 10)   # s = 15, p = 50

x, y = 1, 2
x, y = y, x                     # swap variables


# Dictionaries

empty_dict = {}                     # pythonic
grades = { 'Joel': 80, 'Tim': 95 }  # dictionary
joels_grade = grades['Joel']        # 80
try:                                # you'll get a KeyError if ask for a key 
    kates_grade = grades['Kate']    # that's not in the dictionary
except KeyError:
    print 'no grade for Kate'

joel_has_grade = 'Joel' in grades   # True
kate_has_grade = 'Kate' in grades   # False

joels_grade = grades.get('Joel', 0) # if key is not in dictionary returns 0 which is default value
kates_grade = grades.get('Kate', 0) # 0
no_ones_grade = grades.get('No One')    # if default not specified then is None

grades['Tim'] = 99                  # replaces old value
grades['Kate'] = 100                # add a third entry
num_students = len(grades)          # 3

tweet = {
    'user' : 'chucheria',
    'text' : 'holi',
    'retweet_count': 100,
    'hashtags': ['greetings', 'holi']
}                                   # representing structured data

tweet_keys = tweet.keys()           # list of keys
tweet_values = tweet.values()       



