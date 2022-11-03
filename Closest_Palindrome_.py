n=int(input())
palin=[]

for i in range(10,n*10):
    t=i
    rev=0
    while i>0:
        re=i%10
        rev=rev*10+re
        i=i//10
    if t==rev:
        palin.append(rev)
if n in palin:
    palin.remove(n)
for u in palin:
    if u>n:
        p1=u
        break
palin.reverse()
for k in palin:
    if k<n:
        p2=k
        break
p3=abs(n-p1)
p4=abs(n-p2)
if p3<p4:
    print(p1)
elif p3==p4:
    print(p2,p1)
else:
    print(p2)