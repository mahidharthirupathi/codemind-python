n=int(input())
a=0
b=1
fib=[]
fib.append(int(a))
fib.append(int(b))
for i in range(n-2):
    c=a+b
    fib.append(int(c))
    a=b
    b=c

for j in fib:
    print(j,end=" ")