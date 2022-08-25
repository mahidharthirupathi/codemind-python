a=int(input())
e=a*a
sum=0
while(e>0):
    d=e%10
    sum=sum+d
    e=e//10
if(sum==a):
    print("Neon Number")
else:
    print("Not Neon Number")