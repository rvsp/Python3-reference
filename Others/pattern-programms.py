'''
Owner: Venkatasubramanian
Topic: General & Pattern Programs
'''


import numpy as np

def nxnMatrix(n):
    x = np.zeros((n, n), dtype = int) 
    x[1::2, ::2] = 1
    x[::2, 1::2] = 1
      
    for i in range(n): 
        for j in range(n): 
            print(x[i][j], end =" ")  
        print()  

nxnMatrix(int(input()))



n=int(input())
for i in range(n):
    for j in range(i):
        print('* ', end='')
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end='')
    print('')


# * pattern
n=int(input())
for i in range(0,6):
    for j in range(0,n):
        print(end=' ')
    n-=2
    for j in range(0, i+1):
        print('* ', end='')
    print()


# matrix pattern
x=int(input())
for i in range(0,x):
    for j in range(0,x):
        if i==j:
            print('1',sep=' ',end=' ')
        else:
            print('0',sep=' ',end=' ')
    print()



def is_valid_parenthese(str1):
    stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
    for parenthese in str1:
        if parenthese in pchar:
            stack.append(parenthese)
        elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
            return False
    return len(stack) == 0

print(is_valid_parenthese("(){}[]"))
print(is_valid_parenthese("()[{)}"))
print(is_valid_parenthese("()"))