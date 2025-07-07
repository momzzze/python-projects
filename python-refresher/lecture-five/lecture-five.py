# ---------------------------------- Loops ----------------------------------#

my_list = [1, 2, 3, 4, 5]
sum_for_loop = 0
for item in my_list:
    sum_for_loop += item

print(sum_for_loop)


dates = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for x in dates:
    print(f"Happy {x}!")

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print("i is no longer less than 5, exiting the loop.")

"""
Loops Assignment
Given: my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
- Create a while loop that prints all elements of the my_list variable 3 times.
- When printing the elements, use a for loop to print the elements
- However, if the element of the for loop is equal to Monday, continue without printing
"""

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

i = 0
while i < 3:
    for day in my_list:
        if day == "Monday":
            continue
        print(day)
    i += 1
