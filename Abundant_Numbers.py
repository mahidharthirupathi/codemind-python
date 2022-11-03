n=int(input())
l=[]
sum=0
for i in range(1,n):
    if n%i==0:
        l.append(int(i))
for i in l:
    sum+=i
print(sum>n)