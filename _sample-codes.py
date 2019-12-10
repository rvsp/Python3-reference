
c='string ahsduba sdfbhjsnb bksf hysfb uyfbk'
l=c.split()
s=l[0]+' '+' '.join(str(w[::-1]) for w in l[1:len(l)-1])+' '+ l[len(l)-1]
print(s)


n=int(input())
s=''
for x in range(1,len(c),2):
    s+=c[x-1]
    s+=c[x].upper()
print(s)

sh='i am shery'
x=' '.join(str(w[::-1]) for w in sh.split())
print(x)

vowel='aeiouAEIOU'
x=''.join(l for l in sh if l not in vowel)
print(x.strip())


s='he3l4lo5 world'
d={'num':0,'str':0}
for i in s:
    if i.isnumeric():
        d['num']+=1
    elif i.isalpha():
        d['str']+=1
print(d)


# conver list of tuple to dict
l=[('x',2),('z',1),('y',5),('x',5),('z',5),('y',4),('z',8)]
d={}
for a,b in l:
    d.setdefault(a,[]).append(b)
    # d.setdefault(a,b)
print(d)


# sorted for dict
for k,v in sorted(d.items()):
    print(k,v)

for k in sorted(d):
    print(k,d[k])



d={'d':43,'c':66,'b':23,'a':45}
# largest value in dict using heap
from heapq import nlargest
l= nlargest(1,d,key=d.get)
print(l)



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



def calc(n):
    return n*n

num = (1,2,3,4,5)
result= map(calc, num)
print('Result',list(result))


result1= map(lambda x: x*x, num)
print('Result',list(result1))


a = input()