def decToBin(n):
    binary=0
    i=n
    while(i>0):
        rem =i%2
        binary = binary*10 +rem
        i=i//2
    return int(binary)


num1=float(input("enter a number with base 10 to convert to base 2 or binary : ")
           )
print(decToBin(num1))
        
    
