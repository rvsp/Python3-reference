'''
Owner: Venkatasubramanian
Topic: Encapsulation
'''

class Computer:

    def __init__(self):
        self.__maxprice = 900
        self.tellValue = 342

    def sell(self):
        tellValue=234
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price
    
    def getMaxPrice(self):
        return self.__maxprice

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()