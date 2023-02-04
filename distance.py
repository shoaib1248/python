i=1
print("enter the 1st coordinste:")
while i<=2:
    x=int(input("X:"))
    y=int(input("Y:"))
a=[]
a.append(x)
print("enter the 2nd coordinste:")
while i<=2:
    x=int(input("X:"))
    y=int(input("Y:"))
b=[int(x),int(y)]
d=((int(b[1])-int(a[1]))**2)+((int(b[2])-int(a[2])))**2
import math
print(math.sqrt(d))