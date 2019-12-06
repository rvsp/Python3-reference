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