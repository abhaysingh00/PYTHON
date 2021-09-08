print ("Enter positive even numbers to add.")
sm=0
for i in range(1000000):
    evn=int(input())
    if (evn%2==0):
        if(evn>=0):
            sm=sm+evn
        else:
            print("the sum is",sm)
            break
    if(evn%2!=0):
        print("ERROR")
        print("the sum till now is", sm)
