# ---------------------------------- SETS----------------------------------
# Sets are unordered collections of unique elements.
# What specifics do we need to know about sets?
# 1. Sets do not allow duplicate elements.
# 2. Sets are mutable, meaning you can add or remove elements.
# 3. Sets are unordered, so the elements do not have a specific order.
# 4. Sets are useful for membership testing and eliminating duplicates from a collection.
# 5. Sets can be created using curly braces `{}` or the `set()` constructor.
# 6. Sets support mathematical operations like union, intersection, and difference.

# In the web development world, sets are often used to manage collections of unique items, such as user IDs, tags, or categories.
# In DSA (Data Structures and Algorithms), sets are used for efficient membership testing and to eliminate duplicates from lists or other collections.
# In algo complexity:
# - Adding an element to a set is O(1) on average.
# - Removing an element from a set is O(1) on average.
# - Checking if an element is in a set is O(1) on average.
# - Iterating through a set is O(n), where n is the number of elements in the set.
# - Sets do not support indexing or slicing like lists or tuples.

# Linked Lists with sets:
# Sets are not typically used to implement linked lists, as linked lists are inherently ordered collections that allow for efficient insertion and deletion of elements at both ends.

my_set = {1, 2, 3, 4, 5, 1, 2, 3}  # Duplicates are ignored
print(my_set)
print(len(my_set))

for x in my_set:
    print(x, end=" ")
print()
my_set.discard(3)
print(my_set)
my_set.add(6)
print(my_set)


# ------------------------------------ TUPLES ----------------------------------
# Tuples are ordered collections of elements that are immutable.
# What is immutable?? - It means that once a tuple is created, its elements cannot be changed.
# Are there any exceptions? - Yes, tuples can contain mutable elements like lists.
# Those lists can be modified, but the tuple itself cannot be changed.

# Tuples in web development:
# Tuples are often used to return multiple values from functions, as they can hold a fixed
# number of elements that are not meant to change. Like :
# def get_user_info():
#     return ("John", "Doe", 30)  # Returns a tuple with name, surname, and age
# In DSA, tuples are used to represent fixed collections of items, such as coordinates (x, y) or RGB color values (red, green, blue).
# In algorithm complexity:
# - Accessing an element in a tuple is O(1).
# - Tuples do not support adding or removing elements, so there are no complexities for those operations.
# Tuples do not support indexing or slicing like lists, but you can access elements using their index.
# Linked Lists with tuples:
# Tuples are not typically used to implement linked lists, as linked lists require mutable elements to allow for efficient insertion and deletion of nodes. However, tuples can be used to represent nodes in a linked list, where each tuple contains the data and a reference to the next node.

print("---------------------------------- TUPLES ----------------------------------")

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(len(my_tuple))

my_tuple_with_list = (1, 2, [3, 4, 5])  # Tuple with a mutable list
print(my_tuple_with_list)
my_tuple_with_list[2].append(6)  # Modifying the list inside the tuple
print(my_tuple_with_list)


"""
Lists Assignment
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals

"""
zoo = ["lion", "tiger", "bear", "elephant", "giraffe"]
zoo.pop(3)
zoo.append("zebra")
zoo.pop(0)
print(zoo)
print(zoo[0:3])
