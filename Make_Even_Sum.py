n=int(input())
lst=list(map(int,input().split()))
w=sum(lst)
if (w%2==0):
    print(1)
else:
    print(0)
