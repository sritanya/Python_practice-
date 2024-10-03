# Type conversion :-
"""In programming, type conversion is the process of converting data of one type to another. For example: converting int data to string
There are two types of type conversion in Python.
1. Implicit Conversion - automatic type conversion
2. Explicit Conversion - manual type conversion  """
# Implicit Conversion :-

integer=5
float=5.0
num=integer+float
print(num)
print("datatype",type(num)

# Explicit Conversion :-

num_string='123'
num_integer=234
print("Data type before conversion:-",type(num_string))
num_string=int(num_string)
print("Data type after conversion :-",type(num_string))
sum_number=num_string+num_integer
print("sum",sum_number)
print("data type of the sum_number",sum_number)



