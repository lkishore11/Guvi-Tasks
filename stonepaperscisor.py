import random
coni=["1","2","3"]
con=["stone","paper","scisor"]

flg=True
points=0
count=0
print("Stone paper scisor game")
ch1=int(input("enter the mode\n 1.PC Vs User\n 2.User1 Vs User2\n Mode:"))
if ch1==1:
    print("PC Vs User")
    while(flg):
        a=random.choice(coni)
        print(str(con)+":")
        b=input("enter your choice\n 1.stone\n 2.paper\n 3.scisor\n choice:")
        if b==a:
            print("you won")
            points=points+1
            count=count+1
            ch=input("if u want to exit press q:")
            if(ch=='q'):
                print("The score is ",points)
                print("out of",count)
                flg=False

        else:
            print("wrong")
            count=count+1
            ch=input("if u want to exit press q:")
            if(ch=='q'):
                print("The score is ",points)
                print("out of",count)
                flg=False
    
elif(ch1==2):
    try:
        print("User1 Vs User2")
        rounds=int(input("enter the number of rounds"))
        pl=input("enter player name:")
        points=0
        count=0
        for i in range(rounds):
            a=random.choice(coni)
            print(str(con)+":")
            b=input("enter your choice\n 1.stone\n 2.paper\n 3.scisor\n choice:")
            if b==a:
                print("you won")
                points=points+1
                count=count+1

            else:
                print("wrong")
                count=count+1
    finally:
        print("The score of player",pl,"is",points)
        print("out of",count)

    try:
        print("User1 Vs User2")
        rounds=int(input("enter the number of rounds"))
        pl=input("enter player name:")
        points=0
        count=0
        for i in range(rounds):
            a=random.choice(coni)
            print(str(con)+":")
            b=input("enter your choice\n 1.stone\n 2.paper\n 3.scisor\n choice:")
            if b==a:
                print("you won")
                points=points+1
                count=count+1

            else:
                print("wrong")
                count=count+1
    finally:
        print("The score of player",pl,"is",points)
        print("out of",count)
            
else:
    print ("enter valid options")


    
