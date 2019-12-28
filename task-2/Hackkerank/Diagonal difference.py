n=int(input())
matrix=[]
for i in range(n):
    arr=list(map(int,input().split()))
    matrix.append(arr)
rd=0
ld=0
for j in range(n):
    for k in range(n):
        if(j+k==n-1):
            temp=matrix[j][k]
            rd+=temp
for l in range(n):
    ld+=matrix[l][l]
print(abs(ld-rd))
            
