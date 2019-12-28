m, n, a=input().split()
m=int(m)
n=int(n)
a=int(a)
x=m//a
y=n//a
if (m%a==0):
    m=m
    print(m)
else:
    m=a*(x+1)
    print(m)
    
    
if (n%a==0):
    n=n
    print(n)
else:
    n=a*(y+1)
    print(n)
    
 
z=((m*n)/(a**2))
print(int(z))
