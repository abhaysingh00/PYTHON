def decToBin(n):
    binary=0
    i=int(n)
    count=-1
    while(i>0):
        count+=1
        rem =i%2
        binary =binary +rem *(10**count)
        i=i//2
    return (binary)


num1=float(input("enter a number with base 10 to convert to base 2 or binary : ")
           )
print(decToBin(num1))
        
    
