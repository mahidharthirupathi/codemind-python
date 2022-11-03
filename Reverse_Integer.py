n=int(input())
rev=0
if n>0:
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    print(rev)
    
else:
    n=abs(n)
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    print(rev-(rev*2))