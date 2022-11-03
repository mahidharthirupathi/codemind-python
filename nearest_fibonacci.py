n=int(input())
l=[]
a=0
b=1
for i in range(n*2):
    c=a+b
    l.append(c)
    a=b
    b=c
for k in l:
    if k>=n:
        f1=k
        break
l.reverse()
for u in l:
    if u<n:
        f2=u
        break
f3=abs(n-f1)
f4=abs(n-f2)
if f3==f4:
    print(f2,f1)
elif f3<f4:
    print(f1)
else:
    print(f2)