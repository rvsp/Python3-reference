'''
Owner: Venkatasubramanian
Topic: Inheritance
'''

'''
Inheritance syntax
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
'''

# single inheritance
class Bird:             # parent class
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()


# Multiple Inheritance
class Base1:
    pass
class Base2:
    pass
class MultiDerived(Base1, Base2):
    pass

# multilevel inheritance
class Base:
    pass
class Derived1(Base):
    pass
class Derived2(Derived1):
    pass