# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:49:58 2016

@author: beatriz.hernandez
"""


# Sorting

x = [ 4, 1, 2, 3]
y = sorted(x)           # y = [1, 2, 3, 4]
x.sort()                # x = [1, 2, 3, 4]

# sort the list by absolute value from largest to smallest
x = sorted([-4, 1, -2, 3], key = abs, reverse = True)   # [ -4, 3, -2, 1]

# sort the words and counts from highest count to lowest
wc = sorted(word_counts.item(),
            key = lambda(word, count): count,
            reverse = True)


# List Comprehensions

# Pythonic way of making lists
even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]
squares = [x * x for x in range(5)]  # [0, 1, 4, 9, 16]
even_squares = [x * x for x in even_numbers]    # [0, 4, 16]

# Turn lists into dictionaries or sets
square_dict = {x: x * x for x in range(5)}  # {0: 0, 1: 1, 2: 4, ...}
square_set = {x * x for x in [-1, 1]}   # {1}

# There's no need for the value from the list
zeroes = [0 for _ in even_numbers]  # same length as even_numbers

# Multiple fors in a list comprehension
pairs = [(x, y)
         for x in range(10)
         for y in range(10)]    # (0, 0), (0, 1), ... (9, 8), (9, 9)
         
# For later fors you can use earlier fors
increasing_pairs = [(x, y)      # x < y
                    for x in range(10)
                    for y in range(x + 1, 10)]
                        
                        
# Generators and Iterators
# A generator is something that you can iterate over but 
# whose values are produced only as needed
def lazy_range(n):
    """ a lazy version of range """
    i = 0
    while i < n:
        yield i
        i += 1

for i in lazy_range(10):
    do_something(i)
    
# You can only iterate through a generator once.
    
# Generator using for comprehensions wrapped in parentheses
lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)


# Randomness
import random

four_uniform_randoms = [random.random() for _ in range(4)] 
# [0.7716140317371256,      # random.random() produces numbers
# 0.9067361553516234,       # uniformly between 0 and 1
# 0.8474248438282903,
# 0.29905019156311563]

# You can set an internal state with random.seed 
random.seed(10)
print random.random()       # 0.57140259469

random.randrange(10)        # choose randomly from range(10)
random.randrange(3, 6)      # choose randomly from range(3, 6)

up_to_ten = range(10)
random.shuffle(up_to_ten)   # [2, 6, 7, 0, 3, 9, 8, 1, 5, 4]

# Pick one element randomly
my_best_friend = random.choice(['Alice', 'Bob', 'Charlie'])

# Randomly choose a sample of elements without replacement
winning_numbers = random.sample(range(60), 6)   # [14, 56, 57, 2, 48, 33]


# Regular expressions
import re

print all([                                     # all of these are true
    not re.match('a', 'cat'),                   # 'cat' doesn't start with 'a'
    re.search('a', 'cat'),                      # 'cat' has an a in it   
    not re.search('c', 'dog'),                  # 'dog' doesn't have a 'c' in it
    3 == len(re.split('[ab]', 'carbs')),        # split to ['c', 'r', 's']
    'R-D-' == re.sub('[0-9]', '-', 'R2D2')      # replace digits with dashes
    ])
    

# Object-Oriented Programming
# Let's create the class Set

# by convention, we give classes PascalCase names
class Set:
    
    # these are the members functions
    # everyone takes a first parameter 'self'
    # that refers to the particular Set objec being used
    
    def __init__(self, values = None):
        """ This is the constructor.
        It gets called when you create a new Set.
        You would use it like
        s1 = Set() empty set
        s2 = Set([1, 2, 2, 4]) initialize with values """
        
        self.dict = {}
        
        if value is not None:
            for value in values:
                self.add(value)
            
    def __repr__(self):
        """ this is the string representation of a Set object
        if ou type it at the Python prompt or pass it to str() """
        
        return "Set: " str(self.dict.keys())
        
    # we'll represent membership by being a key in self.dict with value True
    def add(self, value):
        self.dict[value] = True
    
    # value is in the Set if it's a key in the dictionary
    def contains(self, value):
        return value in self.dict
        
    def remove(self, value):
        del self.dict[value]
        

s = Set([1, 2, 3])
s.add(4)
print s.contains(4)
s.remove(3)
print s.contains(3)

