import random


rd=100
att=0
while(rd<=100):
    a =random.randrange(10,20,1)
    b =random.randrange(10,20,1)
    print(a,b)
    d=int(input("guess the difference:"))
    if (d==100):
          print("you quit affter",att,"tries" )
          break
    att=att + 1
    rd=d-(a-b)
    if (rd>=-2 and rd<=2  ):
          if(att==1):
              print("excelent")
    if(rd==0):
        print("successful in",att,"tries")
        break
    if(att==10):
            print("too many attempts")
            break
               
         
    
      

