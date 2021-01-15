
print('String --------------------')

letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!                   # it means 3 * 3 

# Multiline string is created by using triple single (''') or double quotes ("""). See the example below.

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

print('String Concatenation --------------------')

print(letter + ' ' + greeting)

print('String Interpolation / f-Strings (Python 3.6+)--------')
a = 4
b = 3
print(f'{a} + {b} = {a + b}')


print('Accessing Characters in Strings by Index--------')
language = 'Python'
first_letter = language[0]
print(first_letter) # P

print('Accessing Characters in Strings by Index--------')
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   #