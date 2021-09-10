st="A text file (sometimes spelled textfile; an old alternative name is flatfile) is a kind of computer file that is structured as a sequence of lines of electronic text. A text file exists stored as data within a computer file system. ... Text file refers to a type of container, while plain text refers to a type of content."
st1="text"
l=len(st1)
c=0
for i in range(l) :
    if (st1.find("text")>=-1):
        c=c+1
print(c)
