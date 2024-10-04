# Python Special operators
'''Python language offers some special types of operators like the identity operator and the membership operator. They are described below with examples.'''
# 1. Identity operators :-
'''In Python, is and is not are used to check if two values are located at the same memory location.
It's important to note that having two variables with equal values doesn't necessarily mean they are identical.'''

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1)  # prints False
print(x2 is y2)  # prints True
print(x3 is y3)  # prints False
#  2. Membership operator :-
''' In Python, in and not in are the membership operators. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).
In a dictionary, we can only test for the presence of a key, not the value. '''


message = 'Hello world'
dict1 = {1:'a', 2:'b'}
print('H' in message)  # prints True
print('hello' not in message)  # prints True
print(1 in dict1)  # prints True
print('a' in dict1)  # prints False


