arr=input()
arr=list(arr)
if(len(arr)<7):
    print("NO")
else:
    slice=[]
    for i in range(len(arr)):
        temp=arr[i:i+7]
        if(len(temp)==7):
            slice.append(temp)
    yes=[]
    no=[]
    for i in range(len(slice)):
        ones=0
        
        zeroes=0
        for j in range(len(slice[i])):
            if(slice[i][j]=='1'):
                ones+=1
            elif(slice[i][j]=='0'):
                zeroes+=1
        if(ones==7 or zeroes==7):
            yes.append('yes')
        else:
            no.append('no')
    if(len(yes)>0):
        print("YES")
    else:
        print("NO")
            






