# ------------------------------- Dictionaries ------------------------------#
# A dictionary is a collection of key-value pairs.
# Each key is unique and maps to a specific value.

user_dictionary = {
    "username": "john_doe",
    "name": "John",
    "age": 32,
}
print(user_dictionary)
print(user_dictionary.get("username"))  # Accessing a value by its key
print(user_dictionary["name"])  # Accessing a value by its key
user_dictionary["age"] = 33  # Modifying a value
print(user_dictionary["age"])  # Accessing the modified value
print(len(user_dictionary))  # Getting the number of key-value pairs
user_dictionary.pop("age")  # Removing a key-value pair
print(len(user_dictionary))  # Getting the number of key-value pairs after removal


for x, y in user_dictionary.items():  # why .items()?
    print(f"{x}: {y}")

user_dictionary2 = user_dictionary.copy()  # Copying a dictionary
user_dictionary2.pop("username")  # Removing a key-value pair from the copied dictionary
print(user_dictionary)  # Printing the copied dictionary after modification
print(user_dictionary2)  # Printing the original dictionary after modification
"""
Dictionaries Assignment
Based on the dictionary:

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
- Create a for loop to print all keys and values
- Create a new variable vehicle2, which is a copy of my_vehicle
- Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
- Delete the mileage key and value from vehicle2
- Print just the keys from vehicle2
"""

my_vehicle = {"model": "Ford", "make": "Explorer", "year": 2018, "mileage": 40000}

for x, y in my_vehicle.items():
    print(f"{x}: {y}")

vehicle2 = my_vehicle.copy()
vehicle2.get("number_of_tires", 4)
vehicle2.pop("mileage")
print(vehicle2.keys())
