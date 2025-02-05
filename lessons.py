# this is my first python program.
import math

print("hello world!")
print("I like pizza")

# Strings.
first_name = 'John'
food = "pizza"
email = "kalecode2@gmail.com"
print(f"hello my name is {first_name} I like {food} and my email is {email}")

# Integers.
age = 25
quantity = 3
num_of_student = 66
print(f"you are {age} years old")
print(f'you are buying a quantity of{quantity} items')

# Float.
price = 10.99
gpa = 3.2
print(f'the price is ${price}')
print(f'your gpa is {gpa}')

# Boolean.
is_student = False
for_sale = True
is_online = False
print(f'are you a student? {is_student}')

# if-statement.
if is_student:
    print('you are a student!')
else:
    print('you are NOT a student!')

if for_sale:
    print('That item is for sale')
else:
    print('That item is not available')

if is_online:
    print('You are online')
else:
    print('you are not online')

# typecasting.
name = 'john'
age = 25
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# input() = A function that prompts a user to enter data.
# Returns that data entered as a string.
name = input('what is your name?')
age = input('how old are you?')
print(f'Yo! He said his name is {name.upper()}!')
print(f'{name} is {age} years old')

# exercise rectangle area calculation.
length = float(input('Enter the length: '))
width = float(input('Enter the width: '))
area = length * width
print(f'the area is {area}')

# shopping cart program
item = input('what item would you like to buy? ')
price = float(input('what is the price? '))
quantity = int(input('how many would you like to buy? '))
total = quantity * price
print(f'you have bought {quantity} x {item}/s')
print(f'your total is ${total}')

# MadLibs game.
# word create where you create a story.
# by filling blanks with random words.
adjective1 = input('Enter an adjective(description)')
noun1 = input('Enter a noun(person, place, thing')
adjective2 = input('Enter an adjective (description)')
verb1 = input('Enter a verb ending with ing')
adjective3 = input('Enter an adjective (description)')

print(f'Today I went to a {adjective1} zoo.')
print(f'in an exhibit I saw a {noun1}')
print(f'{noun1} was {adjective2} and {verb1}')
print(f'I was {adjective3}')

# arithmetic operators
friends = 0
friends = friends + 1
print(friends)
friends += 1
print(friends)

x = 3.14
y = 4
z = 5

result = round(x)
print(f'round(x) = {result}')
result = max(x, y , z)
print(result)

x = 9
print(math.pi)
print(math.e)
result = int(math.sqrt(x))
print(f'result is {result}')

# circumference of a circle
radius = float(input('Enter a radius for a circle: '))
circumference = 2 * math.pi * radius
print(f'The circumference is {round(circumference, 2)} cm')

# arithmetic operators.
# area of a circle.
radius = float(input('Enter a radius for a circle: '))
area = math.pi * pow(radius, 2)
print(f'The area of the circle is: {round(area, 2)} cm^2')

# area of a triangle.
a = float(input('Enter side A: '))
b = float(input('Enter side B: '))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f'Side C = {c}')

# if-else statement.
age = int(input('Enter your age: '))
if age >= 100:
    print('You are too old sign Up')
elif age >= 19:
    print("You are now signed Up")
elif age < 0:
    print("You are not born yet")
else:
    print("You must be 18+ to sign Up")

name = input('Enter your name: ')
if name == "":
    print("You must enter tour name")
else:
    print(f"Hello {name.capitalize()}")

# python calculator.
operator = input("Enter and operator (+ - / *): ")
num1 = float(int(input("Enter the 1st number: ")))
num2 = float(int(input("Enter the 2nd number")))

if operator == "+":
    result = num1 + num2
    print (round(result, 3))
elif operator == "-":
    result = num1 + num2
    print (round(result, 3))
elif operator == "*":
    result = num1 + num2
    print (round(result, 3))
elif operator == "/":
    result = num1 + num2
    print (round(result, 3))
else:
    print(f"{operator} is not valid operator")

# python weight converter.
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"You weight is: {weight} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"You weight is: {weight} {unit}")
else:
    print("Unit was not valid!")
