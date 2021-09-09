import string
st = input("enter a string: ")
st1=""
for i in st:
    if i in string.punctuation:
        continue
    else:
        st1=st1+i
print(st1)
        
