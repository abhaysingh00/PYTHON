st = input("enter a string: ")
l =len(st)
m=l//2
for i in range(m):
    if (st[i] != st[l-1-i]):
        isPal=False
        break
    else:
        isPal=True
if isPal==True:
     print("the string is  palindrome")
else:
     print("the string is not palindrome")
        
        
    
        
