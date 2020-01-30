def argsms(b,a=10):
    return a+b

print(argsms(6))

def foo2():
    global y
    y = "local"

def printword():
    print('word in another function',y)

foo2()
printword()
# print(y)


x = "global"
def foo():
    global x
    y = "local"
    x = x * 2
    print('value of x',x)
    print(y)
foo()


# recursions
def factorial(n):    
    if n == 1:
        print(n)
        return 1    
    else:
        print (n,'*', end=' ')
        return n * factorial(n-1)

factorial(5)


def calc(n):
    return n*n

num = (1,2,3,4,5)
result= map(calc, num)
print('Result',list(result))


result1= map(lambda x: x*x, num)
print('Result',list(result1))


def convert(list):
    s = [str(i) for i in list] 
    res = int("".join(s)) 
    return(res) 
# Driver code 
list = [1, 2, 3] 
print(convert(list))



# GCD
def gcdrec(a,b):
    if(b==0):
        return a
    else:
        return gcdrec(b,a%b)

print(gcdrec(10,5))

# GCD with looping
def loopgcd(x,y):
    if x>y:
        s=y
    else:
        s=y
    for i in range(1,s+1):
        if((x%i==0) and (y%i==0)):
            gcd =i
    return gcd

print(loopgcd(10,5))