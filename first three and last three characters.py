import string
st = input("enter a string")
print(list(st[0:3]))
last=(st[-3:])
revlast=list(reversed(last))
for i in revlast:
    print(i)
print(revlast)
