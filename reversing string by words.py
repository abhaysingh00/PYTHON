s=input("enter a sentence to reverse: ")
st=s+" "
l = len(st)
word =" "
sentence =""
for i in range(l):
    if st[i].isspace():
        print(word)
        sentence=word + sentence
        word =" "
    else:
        word=word + st[i]
    

print(sentence)
print(l)
print(len(sentence))
