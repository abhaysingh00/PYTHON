def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)
num=int(input("enter a num to find its factorial"))
print(fact(num))
