n=int(input())
l1=[i for i in range(n)]
l2=[]
def comp():
    for i in l1:
        if i*(i+1)==n:
            l2.append('YES')
        
            break
        else:
            l2.append('NO')
    s=sorted(l2,reverse=True)
    for j in s:
        print(j)
        break
            

comp()