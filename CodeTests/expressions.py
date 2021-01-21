import pytest


#  The parameter weekday is true if it is a weekday, and the parameter vacation is true if we are on
#  vacation. We sleep in if it is not a weekday or we're on vacation. Return true if we sleep in.
#  SleepIn(false, false) → true
#  SleepIn(true, false) → false
#  SleepIn(false, true) → true

# Takes two bools in and returns bools

def sleep_in(weekday, vacation):
    if weekday == False or vacation == True:
        return True
    else:
        return False

#  We have two monkeys, a and b, and the parameters aSmile and bSmile indicate if each is smiling.
#  We are in trouble if they are both smiling or if neither of them is smiling. Return true if we
#  are in trouble.
#  MonkeyTrouble(true, true) → true
#  MonkeyTrouble(false, false) → true
#  MonkeyTrouble(true, false) → false


# Takes two bools in and returns bools

def monkey_trouble(a_smile, b_smile):
    if a_smile == True and b_smile == True or a_smile == False and b_smile == False:
        return True
    else:
        return False

# Given 2 int values, return true if either of them is in the range 10..20 inclusive.
# In1020(12, 99) → true
# In1020(21, 12) → true
# In1020(8, 99) → false

# Will take in two ints and return a bool


def in_1020(a, b):
    if a >= 10 and a <= 20 or b >= 10 and b <= 20:
        return True
    else:
        return False


# Below here will be practice problems that have to do with lists

# Given an array of ints length 3, figure out which is larger between the first and last elements
# in the array, and set all the other elements to be that value. Return the changed array.
# MaxEnd3([1, 2, 3]) → [3, 3, 3]
# MaxEnd3([11, 5, 9]) → [11, 11, 11]
# MaxEnd3([2, 11, 3]) → [3, 3, 3]

def max_end_three(num_list):
    x = 0

    output = []

    a = num_list[0]
    b = num_list[2]

    length = len(num_list)

    if a > b:
        while x < length:
            output.append(a)
            x += 1
    else:
        while x < length:
            output.append(b)
            x += 1

    return output

# Return true if the given non-negative number is a multiple of 3 or a multiple of 5.
# (Hint: Think "mod".)
# Or35(3) → true
# Or35(10) → true
# Or35(8) → false


def multiple_of_3_or_5(num):
    if num % 3 == 0 or num % 5 == 0:
        return True
    else:
        return False


# ***** A little bit more advanced *****

# Given ten digits in an array format them to make a phone number. Output will be a formatted string
# make_phone_number([1234567890]) -> (123) 456-7890
# make_phone_number([5463749876]) -> (546) 374-9876
# make_phone_number([1087658471]) -> (108) 765-8471


def make_phone_number(num):
    area = num[0, 2]

    return area
