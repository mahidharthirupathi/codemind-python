n=int(input())
n1=str(n)
l=len(n1)
sum=0
import math as m
while n>0:
     while l>=1:
            r=n%10
            sum+=m.pow(r,l)
            l-=1
            n=n//10

s1=str(int(sum))
print(s1==n1)