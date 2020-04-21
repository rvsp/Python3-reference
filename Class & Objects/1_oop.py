'''
Owner: Venkatasubramanian
Topic: Object Oriented Programming
'''
'''
* Python is a multi-paradigm programming language.
* object has two characteristics 1) attributes and 2) behavior

OOP Principles:
Inheritance     - A process of using details from a new class without modifying existing class.
Encapsulation   - Hiding the private details of a class from other objects.
Polymorphism    - A concept of using common operation in different ways for different data input.
Abstraction     - Both are nearly synonym because data abstraction is achieved through encapsulation.
'''

# 1) Creating Class and Object in Python
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

