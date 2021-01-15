# Variables store data in memory

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME are different variables)

# INVALID variables 
# first-name
# num-1
# 1num

# VALID variables 

print('VALID variables--------------------')

name = 'Ernest'
age = '20'
is_tall = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'name':'Ernest',
   'lastname':'Muroiwa',
   }

# Printing the values stored in the variables

print('First name:', name)
print('Person information: ', person_info)

print('Data Types----------------------')

# Printing out types
print(type('Ernest'))     # str
print(type(name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2,3,4]))     # list
print(type({'name':'Ernest','age':250, 'is_tall':True}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))     
