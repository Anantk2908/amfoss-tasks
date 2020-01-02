n=input()
n=list(n)
for i in range(len(n)):
    n[i]=list(n[i])

numbers='1234567890'
numbers=list(numbers)

for k in range(len(numbers)):
    for l in range(len(n)):
        if(n[l][0]==numbers[k]):
            n[l][0]=int(n[l][0])

if(n[8][0]=="A"):
    if(n[0][0]==1 and n[1][0]==2):
        n[1][0]=0
        n[0][0]=0
    else:
        n.pop(0)
    
    
    
elif(n[8][0]=="P"):
    if(n[0][0]==1 and n[1][0]==2):
        n[1][0]=12
        n.pop(0)
    elif(n[0][0]==1 and n[1][0]==1):
        n[1][0]=11
        n.pop(0)
    else:
        n.pop(0)


n.pop(-1)


##str=""
##for j in range(len(n)):
##    str+=n[j][0]
##print(str)

print(n)
    

    
