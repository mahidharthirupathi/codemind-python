n,m=map(int,input().split())
l1=[]
l2=[]
for i in range(1,n+1):
    if n%i==0:
        l1.append(i)
for j in range(1,m+1):
    if m%j==0:
        l2.append(j)
l3=[]
for i in l1:
    for j in l2:
        if i==j:
            l3.append(i)
l3=sorted(l3,reverse=True)
for i in l3:
    print(i)
    break