s='hello world'
l=''.join(reversed(s))
print(l[0].upper()+l[1:])

x=s[::-1]
print(x[0].upper()+x[1:])

x=''
l=len(s)-1
while l>=0:
    x+=s[l]
    l-=1
print(''+x[0].upper()+x[1:])



# def calc(n):
#     return n*n

# num = (1,2,3,4,5)
# result= map(calc, num)
# print('Result',list(result))


# result1= map(lambda x: x*x, num)
# print('Result',list(result1))


# a = input()