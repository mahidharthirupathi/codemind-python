n=int(input())
l=[]
while n>0:
    r=n%10
    l.append(int(r))
    n=n//10
print(max(l))