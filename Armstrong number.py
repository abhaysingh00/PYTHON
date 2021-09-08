n=int(input())
i=n
cubicSum=0
while(i>0):
    a=i%10
    cubicSum=cubicSum+a*a*a
    i=i//10
print (cubicSum)
if cubicSum==n:
    print("the number",n, "is an armstong number")
else:
    print("the number",n ,"is not an armstong number")
    
