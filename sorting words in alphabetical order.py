st=input("enter a string: ")

words=st.lower().split(" ")
words.sort()
for i in words:
    print(i)


