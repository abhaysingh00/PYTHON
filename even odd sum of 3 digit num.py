n= int(input("enter a three digit number: "))
i=n
sm=0
count=0
while(i>0):
    count=count+1
    sm=i%10+sm
    i=i//10
if(count==3):
    print(sm)
    if(sm%2==0):
        print("the sum is even")
    else:
        print("the sum is odd")
else:
    print("the number entered is not of 3 digits")
    
    
