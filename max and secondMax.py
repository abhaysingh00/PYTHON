n= int(input("enter the number of numbers to be entered"))
l=[]
i=1
max1=0
max2=0
while(i<=n):
    num=int(input())
    l.append(num)
    i=i+1
for j in l:
    if j>max1:
        max2=max1
        max1=j
    elif j>max2:
        max2=j
print("largest number is",max1)
print("second largest number is",max2)
    
    
