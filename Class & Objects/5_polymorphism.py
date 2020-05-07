'''
Owner: Venkatasubramanian
Topic: Polymorphism
'''

class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(t):
    t.fly()

def swim_test(t):
    t.swim()

#instantiate objects
blu = Parrot()
peggy = Penguin()
blu1 = Parrot()

# passing the object
flying_test(blu)
flying_test(peggy)
swim_test(peggy)
swim_test(blu1)