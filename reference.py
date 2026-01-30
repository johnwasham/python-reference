# type: ignore

#=================
# Print
#=================

city = "Paris"

print("I am going to", city, "this weekend") # default sep is " "
print("I am going to", city, "this weekend", sep="-") # I am going to-Paris-this weekend

#=================
# Strings
#=================

greeting_string = "Hello, world!"
first_char = greeting_string[0]  # 'H'
last_char = greeting_string[-1]  # '!'

lowercase_greeting = greeting_string.lower()

my_string = "Hello"
slice_string = my_string[1:3] # "el"

concatenate_string = my_string + ", world!" # "Hello, world!"
repeat_string = my_string * 2 # "HelloHello"

# finding in string

found_in_string = 'l' in my_string.lower() # Returns True
index_in_string = my_string.lower().index('h') if found_in_string else -1 # Returns: 0

name = "  John \t"
name.strip()
name.lstrip()
name.rstrip()

# reverse a string
sentence = "I like coffee"
''.join(reversed(sentence)) # cannot just use reversed()

# iterating

word = 'hello'

for letter in word:
    print(letter) # prints each letter in 'hello'

#====================
# Split / Join
#====================

sentence = 'Python is fun!'
words = sentence.split() # no delimiter provided, splitting by whitespace
print(words)  # Output: ['Python', 'is', 'fun!']

data = 'John,Doe,35,Engineer'
info = data.split(',') # provided a ',' delimiter
print(info)  # Output: ['John', 'Doe', '35', 'Engineer']

words = ['Programming', 'with', 'Python', 'is', 'exciting!']
sentence = ' '.join(words)
print(sentence)  # Output: 'Programming with Python is exciting!'

#====================
# Characters
#====================

print(ord('A'))  # Prints: 65
print(chr(65))  # Prints: 'A'
print(chr(ord('A') + 1)) # Prints: 'B'

print("C".isalpha()) # Prints: True
print("C++".isalpha()) # Prints: False
print("239".isdigit()) # Prints: True
print("C239".isdigit()) # Prints: False
print("C98".isalnum()) # Prints: True
print("C98++".isalnum()) # Prints: False

#====================
# Formatting
#====================

# f string
print(f"I can put {city} in here")

print(" I live in {}".format(city))

average_cost_per_country = 2.75323
print(f"Average: ${average_cost_per_country:.2f}")

# t string

name = "Bob"
age = 40
template = t'Hello {name}, you are {age} years old.'


# Templates

from string import Template

template = Template("Hello, $name! You are $age years old.")
message = template.substitute(name='Bob', age=100)

#====================
# Type Conversions
#====================

num_str = '123'
type(num_str) # Output: <class 'str'>
num = int(num_str)
type(num) # Output: <class 'int'>

age = 8
age_str = str(age);

#=================
# Lists
#=================

dlist = ["Paris", "Sydney", "Tokyo", "New York", "London"]
dlist.insert(1, "Berlin") # inserts at position 1, Sydney moves right
dlist.append("Oslo")
dlist.remove("New York") # removes first occurrence
dlist.pop() # defaults to -1, but can set any index
dlist[3] = "Helsinki" # replace an item

dlist.sort()
dlist.sort(reverse=True)
dlist.reverse()
dlist.sort(key=lambda x: len(x))

foo = [1, 2]
foo.extend([3, 4]) # [1, 2, 3, 4]

large_list = [ ... ]
large_list.copy() # to avoid editing a reference

# initialize with n 1s in a list
n = 6
arr = [1] * n

my_list = [1, 2, 3, 4, 5]
slice_list = my_list[2:4] # [3, 4] first arg is inclusive, second arg is exclusive

concatenate_list = my_list + [6, 7, 8] # [1, 2, 3, 4, 5, 6, 7, 8]
repeat_list = my_list * 2 # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

sorted_list = sorted(my_list, reverse=True) # [5, 4, 3, 2, 1]

# finding in list

natural = ["apple", "butterfly"]

found_apple_in_list = "apple" in natural # Returns: True
found_tree_in_list = "tree" in natural # Returns: False

# get index by item
index_apple_in_list = natural.index("apple") if found_apple_in_list else -1 # Returns: 0
index_tree_in_list = natural.index("tree") if found_tree_in_list else -1 # Returns: -1

# iterating

for i in range(len(natural)):
    print(natural[i])

# With index and value
for i, item in enumerate(dlist):
    print(i, item)

# zip multiple lists (don't need to be same length, will use min length)
nums1 = [1, 3, 5, 8]
nums2 = [2, 4, 6]
nums3 = [1000, 1500, 3000, 5000, 123]
# zip returns a zip object, have to convert to list!
combined = list(zip(nums1, nums2, nums3))

#=================
# Tuples
#=================

# immutable

visited = ("Paris", "London")
visited[0]
visited[-1]

#=================
# Dictionaries
#=================

# remove a key/pair

capitals = {
    "Germany": "Berlin",
    "Japan": "Tokyo"
}

capitals["France"] = "Paris"

del capitals["Germany"]

capitals.popitem() # removes last added (and returns a tuple), in this case: Japan

# Dict comprehension ( note {} and : )
myMap = { i: 2*i for i in range(3) }

destination_events = {
    "France": ["Cannes Film Festival", "Bastille Day Fireworks"],
    "Italy": ["Venice Carnival", "Florence Wine Festival"],
    "Spain": ["La Tomatina", "Running of the Bulls"],
    "Japan": ["Sapporo Snow Festival", "Cherry Blossom Viewing"]
}

destination_events.items() # Return a set-like object providing a view on the dict's items.

# iterating

for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    ...

for destination, events in destination_events.items():
    ...

#=================
# Nested Dicts
#=================

airport_codes = {
    "JFK": {"city": "New York", "country": "USA"},
    "LAX": {"city": "Los Angeles", "country": "USA"},
    "LHR": {"city": "London", "country": "UK"},
    "HND": {"city": "Tokyo", "country": "Japan"},
    "SYD": {"city": "Sydney", "country": "Australia"}
}

print(airport_codes["LHR"]["city"])

#=================
# Range
#=================

for num in range(5):
    # This line will print numbers from 0 to 4
    print(num)

end = 5
start = 0
step = 2
range(end)
range(start, end, step)

# Looping from i = 5 to i = 2
for i in range(5, 1, -1):
    print(i)

print(my_list[::2]) # every other item

print(my_list[::-1]) # reverse list

#=====================
# Gotcha!
#=====================

# if you initialize from lst=[] it will REUSE the list on every call!
# this is how you fix it

def mutation(lst=None):
    if lst == None: 
        lst = []
    lst.append(10)

    return lst

mutation()
mutation()
mutation()
print(mutation())

#=====================
# Comprehensions
#=====================

numbers = '1,2,3,4,5'
num_list = [int(number) for number in numbers.split(',')]
total = sum(num_list)

# how to read it
# [operation for x in iter for y in sub_iter]
# this is similar to a nested for loop with x on outside and y loop inside

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# creates a dict, note the { x: y }
my_dict = {name: hero for name, hero in zip(names, heroes)}
# creates a list of tuple, note the [ () ]
tuple_list = [(name, hero) for name, hero in zip(names, heroes)]
# creates a set of tuple, note the { () }
tuple_set = {(name, hero) for name, hero in zip(names, heroes)}

#=====================
# Generators
#=====================

nums = [1, 3, 5, 8]

def square_generator(nums):
    for n in nums:
        yield n * n

my_gen = square_generator(nums)

# or make it a list comp
my_gen = [n*n for n in nums]

for n in my_gen:
    print(n)

#====================
# Control Structures
#====================

# if else elif
# for boolean conditionals, == or "is" are ok

# elif 500 <= budget <= 1000

#====================
# Loops
#====================

# for else

essential_gadgets = ["laptop", "charger", "adapter", "USB drive"]
packed_items = ["laptop", "USB drive", "notebooks", "pens"]

for gadget in essential_gadgets:
    for packed in packed_items:
        if packed == gadget:
            break
    else: # runs if there was no break called
        print(f"Missing: {gadget}")

#============================
# Cool methods: Map/Filter
#============================

help(print) # displays help page for print()

# strings

list_of_words = ["apple", "mouse", "fox"]  # sets ok too

lengths = map(len, list_of_words)
# convert to list
print(list(lengths))

my_things = map(lambda x: "my " + x, list_of_words)
# convert to list
print(list(my_things))

# ints

list_of_numbers = [24, 6, 83, 36]  # sets ok too
larges = filter(lambda x: x > 30, list_of_numbers)
# convert to list
print(list(larges))

# using a function instead

def multiply(word):
    return word * 3  # like hellohellohello

mult_things_map = map(multiply, list_of_words)
print(list(mult_things_map))

#====================
# Fancy sorting
#====================

# simple
sorted_list = sorted(my_list)

# sorting objects

person_objects = [ 
    # Person objects here
] 

sorted_list = sorted(person_objects, key=lambda person: person.age)

students = [
    ('Alice', 25, 50.5),
    ('Bob', 30, 45.0),
    ('Charlie', 25, 55.0),
    ('David', 30, 45.0)
]

# Sort by age (ascending), then score (descending), then name (ascending)
# To sort in descending order for a specific criterion, negate the value if it's a number.
sorted_students = sorted(students, key=lambda x: (x[1], -x[2], x[0]))

# sorting maps

data = [
    {'name': 'Jake', 'age': 30, 'score': 85},
    {'name': 'Beth', 'age': 25, 'score': 90},
    {'name': 'Mike', 'age': 25, 'score': 95},
    {'name': 'Dave', 'age': 30, 'score': 80}
]

# Sort by age (ascending), then score (descending)
sorted_data = sorted(data, key=lambda item: (item['age'], -item['score']))

data = [
    (400, "zebra"),
    (500, "llama"),
    (500, "horse"),
]

# first element descending, second ascending
s = sorted(data, key=lambda t: (-t[0], t[1]))
# -t[0] turns the first element into a negative value, so larger numbers become 
#   smaller negatives → descending order.
# t[1] is left untouched, giving a normal ascending sort on the animal names.

# first element descending, second descending
s = sorted(data, key=lambda x: (x[0], x[1]), reverse=True)
# it does this by sorting in order ascending for both, then reversing the list

#====================
# Queues
#====================

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()     # Q style
queue.appendleft(1) # Q style
queue.pop()         # deque style

#====================
# Sets
#====================

mySet = set()

mySet.add(1)
mySet.add(2)

mySet.remove(2)

if 2 in mySet:
    print("has 2 in set")

# convert list to set
set([1, 2, 3])

# set comprehension - note {}

mySet = { i for i in range(5) }

#====================
# Tuples
#====================

# Tuples are like arrays but immutable
tup = (1, 2, 3)
print(tup[0])
print(tup[-1])

# Can't modify
# tup[0] = 0

# Can be used as key for hash map/set
myMap = { (1,2): 3 }
print(myMap[(1,2)])

mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)

#====================
# Heaps
#====================

import heapq

minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0
print(minHeap[0])

# heappop() to remove min
while len(minHeap):
    print(heapq.heappop(minHeap))

# No max heaps by default, work around is
# to use min heap and multiply by -1 when push & pop.
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# Build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

#=================
# Functions
#=================

# Nested functions have access to outer variables
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c
    return inner()

print(outer("a", "b"))

# Can modify objects but not reassign
# unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2
        
        # will only modify val in the helper scope
        # val *= 2

        # this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

nums = [1, 2]
val = 3
double(nums, val)

#=================
# Classes
#=================

class MyClass:
    # Constructor
    def __init__(self, nums):
        # Create member variables
        self.nums = nums
        self.size = len(nums)

    # self key word required as param
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()

myObj = MyClass([1, 2, 3])
print(myObj.getLength())
print(myObj.getDoubleLength())

#=================
# DataClasses
#=================

from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
            return self.unit_price * self.quantity_on_hand

#=================
# Random
#=================

import random

rand = random
print(rand.random())
print(rand.randint(1, 6))  # random int between 1 and 6
print(rand.uniform(1, 10))  # random float between 1 and 10
print(rand.choice(["hello", "hola", "안녕하세요"]))  # random greeting
print(rand.choices(["hello", "hola", "안녕하세요"], k=10))  # creates list of 10 random greetings
print(rand.choices(["hello", "hola", "안녕하세요"], weights=[10, 5, 15], k=10))  # sets weights for each (10/30 for example)

nums = [1, 2, 3, 4]
random.shuffle(nums)  # shuffles in place
print(nums)

deck = list(range(1, 53))
hand = random.sample(deck, k=5)  # gimme 5 random unique cards

#=================
# Regex
#=================

import re

sentence = "something"

re.match("test", sentence) # checks for a match only at the beginning of the string
re.search("test", sentence) # checks for a match anywhere in the string (this is what Perl does by default)
re.fullmatch("test", sentence) # checks for entire string to be a match

text = "this is my text\nthis is more"

if re.search("te|th", text):
    print("got em")

# doesn't match, since not at beginning of string
if re.match("my", text):
    print("match got em") # nope it don't

search = re.search(r"my\stext", text)
# print("search:", search)  # just a map object
print("start index:", search.start())
print("end index:", search.end())  # use end - 1 for index

results = re.findall(r"((?:th|te)\w+)", text)  # ?: non-capturing
print(results)  # prints matched portions, across all lines (multiple captures result in tuple for each match)

lines = re.split(r"\s", text)  # split on whitespace
print(lines)

#=====================
# Context Managers
#=====================

# auto-closes file, even in case of exception
with open('sample.txt', 'w') as f:
    f.write('Lorem ipsum')

#=====================
# Files
#=====================

# modes
# r     Read-only. Raises I/O error if file doesn't exist.
# r+    Read and write. Raises I/O error if the file does not exist.
# w     Write-only. Overwrites file if it exists, else creates a new one.
# w+    Read and write. Overwrites file or creates new one.
# a     Append-only. Adds data to end. Creates file if it doesn't exist.
# a+	Read and append. Pointer at end. Creates file if it doesn't exist.

# after using open() with right mode
with open('sample.txt', 'w') as file:
    file.write("hello") # will overwrite file unless using "a" mode

with open('sample.txt', "r+") as file:
    content = file.read()
    print(content)
    file.write("hello") # appends since pointer is at end

# for append, add \n to put on new line

#=================
# MultiProcessing
#=================


#=================
# Rounding
#=================

rounded = round(5.2347)
rounded = round(5.2347, 2)

# cut off decimal places
some_int = int(5.7232) # 5

#=================
# Math
#=================

floaty = 10 / 4   # 2.5
floory = 10 // 4  # 2

import math

print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2, 3))

# Max / Min Int
float("inf")
float("-inf")

x = 5.3626

math.floor(x)
math.ceil(x)

# Exponentiation

2**2 == 4  # proper exponentiation
2^2 == 0 # NO!! BITWISE OR

#=================
# Misc
#=================

some_variable = "hello"
repr(some_variable) # acts like print_r in php
