def sum(a, b):
    print("sum is", a+b)

# **kwargs
def my_func(**kwargs):
    for i, j in kwargs.items():
        print(i, j)

my_func(name='tim', sport='football', roll=19)

# not possible with kargs & args
# print(dir(kargs))
# print(dir(**kargs))


# *args and **kwargs in function call

def my_three(a, b, c):
    print(a, b, c)

x = [1,2,3]
my_three(*x)


def my_three(a, b, c):
    print(a, b, c)

a = {'a': "one", 'b': "two", 'c': "three" }
my_three(**a)



# *args
def sum(*args):
    s = 0
    for i in args:
        s += i
    print("sum is", s)

print(sum(1, 2, 3))
print(sum(1, 2, 3, 4, 5, 7, 8, 9, 10))
print(sum())