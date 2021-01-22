# Here you can get some practice creating and naming lists and dictionaries. These are very important and you will use them often in any language.

# https://www.w3schools.com/python/python_lists.asp here is the link to the W3 wchools list page. It will help
# Example of a list game_consoles_list = ['Xbox', 'Playatation', 'Sega Dreamcast']
#                                           0           1               2
#                                         Remember a list has a 0 based index
#  Lists can be any many data types (int, float, string, etc)
#  The list methods section of W3 schools is a great resource to see what type of operations you can do on lists.

# You are able to do all the below things to this list of nums as well. Be aware that list can be of multiple types but then they become a whole seperate data type.
#  For now stick with lists of one data type.
# Mess around with the cars list primarily but check out operations on both lists.
nums_list = [1, 2, 3, 4, 5, 67, 8, 89, 4, 343434, 56]

# Create a list of your favorite car brands (At least 7) | Use this one or make your own for practice.
cars_list = ['Volvo', 'Porsche', 'BMW', 'Pagani', 'Chrysler', 'Dodge', 'Jeep']

# Get the 4th list item and print it out.
# Example - print(cars_list[3])

# You can change the list item by accessing it and assigning it like a variable.
# Example - cars_list[1] = 'Ferrari' That list item will now be Ferrari.
# Change the 5th list item to your least favorite brand.


# You can also add items to a list. Append and item or two to the end of the list. You can use print(len(cars_list)) to check the length and make sure items are being added.
# This will use the append Method
# Example - cars_list.append('Kia') this will add Kia to the end of the list.


# There are other ways to insert values into a list but for know we will leave it at that.


# You can remove items from the list as well. Using the remove() Method.
# Example - cars_list.remove('Kia') will remove the item from the list.


# The pop() method will remove a list item at a specfic index. Remove and item from the list.
# Example cars_list.pop(1) If you do not specify and index it will remove the last item on the list.


# Looping through lists

# The most basic for loop for a list just loops through the list and prints out each item to the terminal. Do that to see all the changes you made to the original list.
# for x in cars_list:
#     print(x)


# Now sort the list using the sort method and loop through it again to see the changes.
# The sort method works alphabeticaly with strings and numerically with number types (int, float).
# You can sort ascending or descendin.
# Check out the W3 Schools for list sorting there are to many methods to example here.
# change the print statment at the end to see all the list changes.

# Sort the list in ascending order.

# Sort the list in descending order.


# Sort the list case insensitevely? Spelled that wrong, you get the idea.

# Reverse the list

# Example - print(cars_list) you can print this and it will change each time you modify the list.
