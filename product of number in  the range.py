m=int(input("enter num1"))
n=int(input("enter num2"))
prod=1
for i in range(m,n+1):
    d=i
    while(d>0):
        prod=prod*(d%10)
        d=d//10
        print (prod)
    prod=1
