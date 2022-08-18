a,b=map(int,input().split())
c=a+1
d=b+1
if(c==b) or (d==a):
    print("Yes")
elif(a+b==11):
    print("Yes")
else:
    print("No")