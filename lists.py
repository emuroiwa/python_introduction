# There are four collection data types in python :

# List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
# Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
# Set: is a collection which is unordered, unindexed and unmodifiable, but you can add new items. No duplicate members.
# Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

print('How to Create a List------------')
# syntax
lst = list()

# syntax
lst = []

fruits = ['banana', 'orange', 'mango', 'lemon']   
# Print the lists and its length
print('Fruits:', fruits)

print('Modifying Lists------------')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']


print('Checking Items in a List------------')
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

print('Removing Items from a List------------')
fruits.remove('banana')
print(fruits)

fruits.pop(0)
print(fruits) 

del fruits[0]
print(fruits) 

print('Joining Lists------------')
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)

print('Sorting List Items------------')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)
