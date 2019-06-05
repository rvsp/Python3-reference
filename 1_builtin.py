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

import sys

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


