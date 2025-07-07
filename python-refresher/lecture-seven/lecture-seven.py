# ----------------------------- Functions ------------------------------#

print("---------------")  # This is a built-in function that prints to the console


def my_function():
    print("This is my function")


my_function()


def print_my_name(name, last_name):
    print(f"Hello {name} {last_name}!")


print_my_name("Nikola", "Ninov")


"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values
"""


def create_person_dict(firstname, lastname, age):
    return {"firstname": firstname, "lastname": lastname, "age": age}


# Example usage
person = create_person_dict("Nikola", "Ninov", 30)
