a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
i,j=1,1
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        if j<=i:
            j=i
    i+=1
print(j)        