def gcdrec(a,b):
    if(b==0):
        return a
    else:
        return gcdrec(b,a%b)

print(gcdrec(10,5))



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