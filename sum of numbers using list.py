l=[]                
for i in range(3): #to run the loop 3times
    l.append(int(input("enter a number")))
if l[0]==l[1]==l[2]: #to check if all the three values are same
    print(3*sum(l)) #to print 3 times the sum of the numbers 
else:
    print(sum(l))

             
