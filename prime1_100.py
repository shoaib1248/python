x=1
while x<=100:
    i=1
    count=0
    while i<=x:
        if x%i==0:
            count+=1
        i+=1
    if count==2:
        print(x)
    x+=1