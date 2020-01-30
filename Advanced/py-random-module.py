'''
Owner: Venkatasubramanian
Topic: Random module
'''

import random as rand

print(rand.random())

print(rand.randint(1,20))

print(rand.randrange(2,20,4))

print(rand.choice((12,23,45,67,65,43)))
print(rand.choice('computer'))

numbers=[12,23,45,67,65,43]
print(rand.shuffle(numbers))


print('Random number from 0 to 1 :', rand.random())
print('Uniform Distribution [1,5] :', rand.uniform(1, 5))
print('Gaussian Distribution mu=0, sigma=1 :', rand.gauss(0, 1))
print('Exponential Distribution lambda = 1/10 :', rand.expovariate(1/10))

string = "inconvenience"
l = [1, 2, 3, 4, 10, 15]
print('Randomly chosen 4 character from string :', rand.sample(string, 4))
print('Randomly chosen 4 length list :', rand.sample(l, 4))

# returns an integer in the specified size (in bits).
print(rand.getrandbits(8))
