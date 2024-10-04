# spilt the bill in between the friends

"""def bill_split(amount, friends):
    tax=(20/100) * amount
    tot = amount + tax
    amount1 = tot/friends
    return amount1
result = bill_split(1000,4)
print(result)"""

# Print true if string first and last letter was same

"""def check_chars(s):
    if s[0]==s[-1]:
        return True
    else:
        return False
result = check_chars('chaitanya')
print(result)"""

# print Add the two number

num1=2.0
num2=3.0
sum=num1+num2
print(f "The sum of  {num1} and {num2} is {sum}")

# print Add two number with user input

num1 = float(input("Enter a new number"))
num2 = float(input("Enter a new number"))
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")

# print the positive number

number = int(input('Enter a number: '))
if number > 0:
    print(f'{number} is a positive number.')
elif number > 0:
    print(f"{number} is a negative number ")
else:
    print(f"{number} is a zero")
print('A statement outside the if statement.')


# Another method for if_else method programme

age=30
salary=50000
if age>=35 and salary>=60000 :
    print("Eligible for this job")
else:
    print("Not Eligible for this Job")





