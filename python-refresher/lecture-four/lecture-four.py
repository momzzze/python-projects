# --------------------------------Booleans and Operators--------------------------------
# They are often used in conditional statements and logical operations.

like_coffee = True
like_tea = False
favorite_food = "Pizza"
favorite_number = 22

print(like_coffee)
print(like_tea)
print(type(like_coffee))
print(type(favorite_food))
print(type(favorite_number))

print(
    favorite_food == favorite_number
)  # This will print False because they are different types
print(
    favorite_food != favorite_number
)  # This will print True because they are different types

# Comparison Operators
print(1 < 2)
print(1 == 2)
print(1 != 2)
print(1 > 2)
print(1 <= 2)
print(1 >= 2)

# logical operators
print(1 > 3 and 2 < 3)  # This will print False because 1 is not greater than 3
print(1 > 3 or 2 < 3)  # This will print True because 2 is less than 3
print(not (1 > 3))  # This will print True because 1 is not greater than 3


# ------------------------------------------- If Statements --------------------------------
print("---------------------------- If Statements -----------------------------")
x = 2

if x == 1:
    print("x is 1")
elif x == 2:
    print("x is 2")
    print("x is 2")
else:
    print("x is neither 1 nor 2")

"""
- Create a variable grade holding an integer between 0 - 100
- Code if, elif, else statements to print the letter grade of the number grade variable
Grades:
A = 90 - 100
B = 80 - 89
C = 70-79
D = 60 - 69
F = 0 - 59
Example:
if grade = 87 then print('B')
"""

grade = 87

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
