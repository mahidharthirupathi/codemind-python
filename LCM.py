a,b=map(int,input().split())
if a>b:
    max=a
else:
    max=b
while(True):
    if(max%a==0 and max%b==0):
        lc=max
        break
    max+=1
print(lc)