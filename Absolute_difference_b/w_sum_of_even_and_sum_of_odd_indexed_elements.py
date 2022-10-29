n=int(input())
lst=list(map(int,input().split()))
a=0
c=0
for i in range(n):
    if i%2==0:
        a+=lst[i]
    else:
        c+=lst[i]
print(abs(a-c))