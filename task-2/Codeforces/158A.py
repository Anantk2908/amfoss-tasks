n,k=input().split()
n=int(n)
k=int(k)
arr=list(map(int,input().split()))[:n]
adv=[]
if (arr.count(arr[k-1]) == len(arr) and arr[k-1]==0):
    print("0")
else:
    
    if(arr[k-1]>=0):

        for i in range(n):
                if(arr[i]>=arr[k-1] and arr[i]>0):
                    adv.append(arr[i])
        print(len(adv))

    #else:
        #print("0")
        
        
