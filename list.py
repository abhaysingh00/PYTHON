n = int(input("the number of elements: "))
num=[]
for i in range(n):
    inp =float(input())
    num.append(inp)
sum=0
even=[]
odd=[]
for var in num:
    sum=sum+var
    if(var%2==0):
        even.append(var)
    else:
        odd.append(var)
print("list of even numbers",even)
print("list of odd numbers",odd)
print("the sum is",sum  )
