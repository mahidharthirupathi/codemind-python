n=int(input())
rev=0
t=n*n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
a=rev*rev
rev1=0
while a>0:
    r=a%10
    rev1=rev1*10+r
    a=a//10
if t==rev1:
    print('True')
else:
    print('False')
    