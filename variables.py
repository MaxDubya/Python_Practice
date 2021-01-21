# IGONRE FOR NOW WE WILL GO OVER IMPORTS LATER
import string as s
alphabet = s.ascii_lowercase

# Comments in python begin with a pound sign and a space. Anything you put after the pound sign will not be ran.
# Comments can be put in blocks like this to give a good description of the code that you are writing below.

# Variables

# Strings

name = 'Max'

my_name = 'Ricky'

name = 'John'


# Numeric types
# The numeric types in python are int, float, complex **I have not had to use complex yet so I am not going to go over it**

max_lucky_number = 13
ricky_lucky_number = 14

dec = 13.55465465

# print(max_lucky_number + ricky_lucky_number / 12 * 43 - dec)

# print(ricky_lucky_number / dec)


# Sequence types / Collections
# In python there are lists, tuples, sets and frozensets
# **The only data type that I have really used extensivly is the list I can explain tuples, sets and frozensets but I don't have great examples**

# Lists
# Use the alphabet list for demo

car_list = ['Ford', 'Chevy', 'Daewoo', 'Hyundai', 'Mutsubishi', 'Volvo']


for item in car_list:
    print(item)

if len(car_list) < 3:
    print("List is larger than three")

print(len(name))

max_lucky_number = max_lucky_number + 5

# Tuples
# **A tuple is a collection which is ordered and unchangeable. Tuples ALLOW duplicate values**


# Sets
# **Sets are unordered, unchangeable and DO NOT allow duplicate values

# Mapping types
# The only mapping type in python is a dictionary


# cardict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "top_speed": 5
# }

# print(cardict['brand'])


boolean = 3 > 4 and 4 < 3

print(boolean)

print('\n-------------------------------------------------------------------\n')

# Under here there will be some simple variable tests that you can run. I will have them hooked up to test so that you can run them.
