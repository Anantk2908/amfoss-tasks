
def  compareTriplets(a,b):
    result=[0,0]
    if(a[0]>b[0]):
        result[0]+=1
    elif(a[0]<b[0]):
        result[1]+=1
    if(a[1]>b[1]):
        result[0]+=1
    elif(a[1]<b[1]):
        result[1]+=1
    if(a[2]>b[2]):
        result[0]+=1
    elif(a[2]<b[2]):
        result[1]+=1
    print(result[0],result[1])

a=list(map(int,input().split()))
b=list(map(int,input().split()))
compareTriplets(a,b)
