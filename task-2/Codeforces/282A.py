X=0
n=int(input())

for i in range(n):
    a=input()
    if(a=="X++" or a=="++X"):
        X+=1
    elif(a=="X--" or a=="--X"):
        X-=1
print(X)
    
