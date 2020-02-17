'''
Owner: Venkatasubramanian
Topic: Built-In Functions
'''

'''
abs()	        returns absolute value of a number
bin()	        converts integer to binary string
chr()	        Returns a Character (a string) from an Integer
complex()       Creates a Complex Number
dir()           Tries to Return Attributes of Object
divmod()        Returns a Tuple of Quotient and Remainder
enumerate()	    Returns an Enumerate Object
eval()	        Runs Code Within Program
filter()        constructs iterator from elements which are true
format()        returns formatted representation of a value
hash()          returns hash value of an object
hex()	        Converts to Integer to Hexadecimal
iter()	        returns an iterator
next()	        Retrieves next item from the iterator
map()	        Applies Function and Returns a List
oct()	        returns the octal representation of an integer
ord()	        returns an integer of the Unicode character
pow()	        returns the power of a number
reversed()      returns the reversed iterator of a sequence
round()         rounds a number to specified decimals
slice()         returns a slice object
sorted()        returns a sorted list from the given iterable
sum()           Adds items of an Iterable
'''


# abs()
integer = -20           # random integer
print('Absolute value of -20 is:', abs(integer))
floating = -30.33       #random floating number
print('Absolute value of -30.33 is:', abs(floating))

# bin()
number = 5
print('The binary equivalent of 5 is:', bin(number))

# chr()
print(chr(65))
print(chr(102))

# complex()
z = complex(2, -3)
print(z)
z = complex(1)
print(z)
z = complex()
print(z)
z = complex('5-9j')
print(z)

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

# divmod()
print('divmod(8, 3) = ', divmod(8, 3))
print('divmod(3, 8) = ', divmod(3, 8))
print('divmod(5, 5) = ', divmod(5, 5))
# divmod() with Floats
print('divmod(8.0, 3) = ', divmod(8.0, 3))
print('divmod(3, 8.0) = ', divmod(3, 8.0))
print('divmod(7.5, 2.5) = ', divmod(7.5, 2.5))
print('divmod(2.6, 0.5) = ', divmod(2.6, 0.5))

# enumerate()
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)
print(type(enumerateGrocery))
# converting to list
print(list(enumerateGrocery))
# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

# eval
def dump_eval(expression):
    result = eval(expression)
    print (expression, "=>", result, type(result))

dump_eval("1")
dump_eval("1.0")
dump_eval("'string'")
dump_eval("1.0 + 2.0")
dump_eval("'*' * 10")
dump_eval("len('world')")


# filter()
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]
result = list(filter(lambda x: (x % 13 == 0), my_list))  
print(result)
palin_list = ["loyol", "fruit", "lol", "practice", "aa"]
result = list(filter(lambda x: (x == "".join(reversed(x))), palin_list))
print(result)

# format()
print(format(123, "d"))
# float arguments
print(format(123.4567898, "f"))
# binary format
print(format(12, "b"))


# hash()
# hash for integer
print('Hash for 181 is:', hash(181))
# hash for decimal
print('Hash for 181.23 is:',hash(181.23))
# hash for string
print('Hash for Python is:', hash('Python'))


# hex()
number = 435
print(number, 'in hex =', hex(number))
number = 0
print(number, 'in hex =', hex(number))
number = -34
print(number, 'in hex =', hex(number))
returnType = type(hex(number))
print('Return type from hex() is', returnType)


# iter() and next()
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_iter = iter(vowels)
print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))

# map()
def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)
# converting map object to set
numbersSquare = set(result)
print(numbersSquare)


# oct()
print('oct(10) is:', oct(10))           # decimal to octal
print('oct(0b101) is:', oct(0b101))     # binary to octal
print('oct(0XA) is:', oct(0XA))         # hexadecimal to octal


# ord()
print(ord('5'))
print(ord('A'))
print(ord('$'))


# pow()
print(pow(2, 2))                    # positive x, positive y (x**y)
print(pow(-2, 2))                   # negative x, positive y
print(pow(2, -2))                   # positive x, negative y
print(pow(-2, -2))                  # negative x, negative y


# reversed()
# for string
seq_string = 'Python'
print(list(reversed(seq_string)))
# for tuple
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seq_tuple)))
# for range
seq_range = range(5, 9)
print(list(reversed(seq_range)))
# for list
seq_list = [1, 2, 4, 3, 5]
print(list(reversed(seq_list)))


# round()
# for floating point
print(round(10.7))
# even choice
print(round(5.5))


# slice()
py_string = 'Python'
slice_object = slice(3) 
print(py_string[slice_object])  # Pyt
# start = 1, stop = 6, step = 2
# contains 1, 3 and 5 indices
slice_object = slice(1, 6, 2)
print(py_string[slice_object]) 


# sorted()
fruits = ['lime', 'blueberry', 'plum', 'avocado']
print(sorted(fruits))
print(sorted(fruits, reverse=True))

# sum()
numbers = [2.5, 3, 4, -5]
numbers_sum = sum(numbers)
print(numbers_sum)
numbers_sum = sum(numbers, 10)
print(numbers_sum)