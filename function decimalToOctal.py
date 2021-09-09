def decToOctal(n):
    octal=0
    i=int(n)
    j=n-i
    count =-1
    while(i>0):
        count=count+1
        rem =i%8
        octal=   octal + rem*(10**count)
        i=i//8
    for k in range(1,5):
        j=j*8
        affterpoint=int(j)
        j=j-affterpoint
        octal=octal+ affterpoint*(10**(-1*k))
      
    
    return octal


num1=float(input("enter a number with base 10 to convert to base 8 or octal : ")
           )
print(decToOctal(num1))
