def ugly(n):
    while n%2==0:
        n=n//2
    if n==1:
        return "Ugly Number"
    while n%3==0:
        n=n//3
    if n==1:
        return "Ugly Number"
    while n%5==0:
        n=n//5
    if n==1:
        return "Ugly Number"  
    return "Not Ugly Number"
    
n=int(input())
print(ugly(n))