i =11
a=b=0
while i>0:
    a=a+i%2
    b=b+min(a,i)
    i=i/2
    print(a,b)