n=int(input())
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)
multiples=[]
for j in range(n):
    temp=[]
    for k in range(arr[j]):
        if(k%5==0):
            temp.append(k)
        elif(k%3==0):
            temp.append(k)
        else:
            continue
    multiples.append(temp)
sum=[]
for i in range(len(multiples)):
    add=0
    for k in range(len(multiples[i])):
        add+=multiples[i][k]
    sum.append(add)
for l in sum:
    print(l)
