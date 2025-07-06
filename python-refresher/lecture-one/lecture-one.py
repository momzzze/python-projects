# --------------------------------VARIABLEs--------------------------------

cost =10
tax_percent=.25
tax=cost * tax_percent
price=cost + tax
print(price)

username="ninov"
first_name="Nikola"
print(username)
print(first_name)

print(username + " " + first_name)
print(f"{username} {first_name}") # same as `${}` in JavaScript


first_num=10
second_num=2
print(first_num)
print(second_num)
first_num=1
print(first_num)
print(second_num)

# with strings

first_name = "Nikola"
second_name= "Ninov"
print(first_name)
print(second_name)

#----------------------------------COMMENTS--------------------------------

# This is a single line comment
# print("This line is commented out and will not run")
# This is a multi-line comment

"""
    This is a multi-line comment
    It can span multiple lines      
"""

#----------------------------------Assignment--------------------------------
"""
Write a Python program that can do the following:
- You have $50
- You buy an item that is $15, that has a 3% tax
- Using the print()  Print how much money you have left, after purchasing the item.
"""

total_money=50
item_cost=15
tax__percent=0.03
tax=item_cost*tax__percent
total__cost=item_cost + tax
left_money=total_money - total__cost


print(left_money)
print(total_money - item_cost - (item_cost*tax__percent))

#----------------------------------STRING FORMATTING--------------------------------

first_name="Nikola"
print(f"Hi {first_name}")

setnence="Hi {} {}"
last_name="Ninov"
print(setnence.format(first_name,last_name))
print(setnence.format(last_name,first_name))