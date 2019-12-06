# def argsms(b,a=10):
#     return a+b

# print(argsms(6))

# def foo2():
#     global y
#     y = "local"

# def printword():
#     print('word in another function',y)

# foo2()
# printword()
# print(y)


# x = "global"
# def foo():
#     global x
#     y = "local"
#     x = x * 2
#     print('value of x',x)
#     print(y)
# foo()







def convert(list):
    s = [str(i) for i in list] 
    res = int("".join(s)) 
    return(res) 
# Driver code 
list = [1, 2, 3] 
print(convert(list))




