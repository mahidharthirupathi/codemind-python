n=int(input())
s=1
s1=0
while(n>0):
    n1=n%10
    s=s*n1
    s1=s1+n1
    n=n//10
print(s-s1)
    
    