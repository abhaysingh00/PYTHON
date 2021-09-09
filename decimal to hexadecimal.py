replacement =['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
n =float(input("enter a number: "))
i=n
hexa=""
while(i>0):
    rem=int(i%16)
    hexa=replacement[rem] +hexa
    i=i//16
print(hexa)
    
