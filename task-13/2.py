def create_fib(d):
  temp=[]
  a=1
  b=2
  c=0
  while c<=d:
    c=a+b
    a=b
    b=c
    temp.append(a)
  return(temp)

n=int(input())
ipt=[]
for i in range(n):
  a=int(input())
  ipt.append(a)


fibonacci=[]
for j in range(len(ipt)):
  s=create_fib(ipt[j])
  fibonacci.append(s)

output=[]
for k in range(len(fibonacci)):
  sum=0
  for l in range(len(fibonacci[k])):
    if(fibonacci[k][l]%2==0):
      sum+=fibonacci[k][l]
  print(sum)

