'''
Owner: Venkatasubramanian
Topic: Built-In Functions
'''

import sys

# https://www.programiz.com/python-programming/methods/built-in/bin


# apply function
def function(a, b):
    print( a, b)

apply(function, ("whither", "canada?"))
apply(function, (1, 2 + 3))

# __import__ function to get a named function

def getfunctionbyname(module_name, function_name):
    module = __import__(module_name)
    return getattr(module, function_name)

print( getfunctionbyname("dumbdbm", "open")) 

# reload function
import hello
reload(hello)

# dir function
def dump_sys(value):
    print( value, "=>", dir(value))


dump_sys(0)
dump_sys(1.0)
dump_sys(0.0j) # complex number
dump_sys([]) # list
dump_sys({}) # dictionary
dump_sys("string")
dump_sys(len) # function
dump_sys(sys) # module

# object's type function
def dump_type(value):
    print (type(value), value)

dump_type(1)
dump_type(1.0)
dump_type("one")

# eval function
def dump_eval(expression):
    result = eval(expression)
    print (expression, "=>", result, type(result))

dump_eval("1")
dump_eval("1.0")
dump_eval("'string'")
dump_eval("1.0 + 2.0")
dump_eval("'*' * 10")
dump_eval("len('world')")


# lambda
rem = lambda num: num % 2
print(rem(5))

def testfunc(num):
  return lambda x : x * num

result2 = testfunc(1000)
print(result2(9))

# map()
numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]
mapped_list = list(map(lambda num: num % 2, numbers_list))
print(mapped_list)

# filter()
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]
result = list(filter(lambda x: (x % 13 == 0), my_list))  
print(result)

palin_list = ["loyol", "fruit", "lol", "practice", "aa"]
result = list(filter(lambda x: (x == "".join(reversed(x))), palin_list))
print(result)


# reduce()
from functools import reduce
def do_sum(x1, x2):
    return x1 + x2

print(reduce(do_sum, [1, 2, 3, 4]))

# sorted()
fruits = ['lime', 'blueberry', 'plum', 'avocado']
print(sorted(fruits))
print(sorted(fruits, reverse=True))

# chr()
print(chr(65))
print(chr(102))