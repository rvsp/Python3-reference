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

 - Single Inheritance
 - Overriding Methods
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


#definition of the class starts here 
class Person:  
    #defining constructor  
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  
  
    #defining class methods  
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
  
# defining another class  
class Student: # Person is the  
    def __init__(self, studentId):  
        self.studentId = studentId  
  
    def getId(self):  
        return self.studentId  

# class Person & Student derived in Resident class  
class Resident(Person, Student): # extends both Person and Student class  
    def __init__(self, name, age, id):  
        Person.__init__(self, name, age)  
        Student.__init__(self, id)  
  
# Create an object of the subclass  
resident1 = Resident('John', 30, '102')  
resident1.showName()  
print(resident1.getId()) 


# multilevel inheritance
class Base:
    pass
class Derived1(Base):
    pass
class Derived2(Derived1):
    pass