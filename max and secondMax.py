n= int(input("enter the number of numbers to be entered"))
l=[]
i=1
max1=0
max2=0
while(i<=n):
    num=int(input())
    l.append(num)
    i=i+1
for j in range(n):
    if l[j]>max1:
        max2=max1
        max1=l[j]
        pos1=j+1
        
    elif l[j]>max2:
        max2=l[j]
        pos2=j+1
print("largest number is",max1, "at position",pos1)
print("second largest number is",max2, "at position", pos2)
    
    
