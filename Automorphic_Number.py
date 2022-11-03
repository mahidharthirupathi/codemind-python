n=input()
n1=int(n)
t=len(n)
i=0
sqr=(n1**2)

l=[]
l1=[]
while n1>0:
    r=n1%10
    l1.append(r)
    n1=n1//10
l1.reverse()

while sqr>0:
    re=sqr%10
    l.append(re)
    sqr=sqr//10
    i+=1
    if i==t:
        break
l.reverse()
if (l==l1):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')