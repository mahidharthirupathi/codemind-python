p,r,t=map(int,input().split())
import math as m
a=p*(pow((1+(r/100)),t))
a1=("{:.2f}".format(a))
print(a1)