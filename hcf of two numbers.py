x=int(input())
y=int(input())
if x>y:
    lesser=y
else:
    lesser=x
for i in range(1,lesser+1):
    if((x%i==0)and (y%i==0)):
        hcf=i
print("hcf of", x,"and",y,"is",hcf)
