a=int(input())
lst=list(map(int,input().split()))
sum=0
for i in (lst):
    sum=sum+i
b=sum//len(lst)
if b in lst:
    print('True')
else:
    print('False')
    