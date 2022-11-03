n=int(input())
pro=0
while 1:
    while n>0:
        r=n%10
        pro+=r*r
        n=n//10
    if pro<10 and pro==1:
        print('True')
        break
    elif pro<10 and pro!=1:
        print('False')
        break
    else:
        n=pro
        pro=0