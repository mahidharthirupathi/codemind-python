n=int(input())
a=0
b=1
fib=[]
fib.append(a)
fib.append(b)
for i in range(n+1):
    c=a+b
    fib.append(c)
    a=b
    b=c
e=[]
for i in fib:
    if i==n:
        e.append('True')
    else:
        e.append('False')
e=sorted(e,reverse=True)
for i in e:
    print(i)
    break