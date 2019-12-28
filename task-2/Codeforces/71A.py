x=int(input())
 
for i in range(x):
    z=input()
    s=list(z)
    
    if(len(s)<=10):
        print(z)
        
    else:
        a=str((len(s)-2))
        r=s[0]+a+s[-1]
        print(r)
