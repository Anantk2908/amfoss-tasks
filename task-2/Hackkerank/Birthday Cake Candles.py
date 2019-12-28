n=int(input())
arr=list(map(int,input().split()))[:n]
h=max(arr)
count=0
for i in range(len(arr)):
    if(arr[i]==h):
        count+=1
print(count)
