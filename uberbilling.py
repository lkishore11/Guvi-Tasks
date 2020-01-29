flg=True
while(flg):
    print("\n\nSelect a Service\n 1.auto\n 2.bike\n 3.car\n 4.exit\n")
    ch=int(input("enter your choice"))
    if(ch==1):
        kms=int(input("enter the distance covered:"))
        if(kms<=1):
            price=20
            print("the bill amount is",price)
        elif(kms<=4):
            rate=18
            price=kms*rate
            print("the bill amount is",price)
        elif(kms>4):
            rate=15
            price=kms*rate
            print("the bill amount is",price)
        else:
            print("enter the valid options")
    elif(ch==2):
        kms=int(input("enter the distance covered:"))
        if(kms<=1):
            price=20
            print("the bill amount is",price)
        elif(kms<=4):
            rate=12
            price=kms*rate
            print("the bill amount is",price)
        elif(kms>4):
            rate=15
            price=kms*rate
            print("the bill amount is",price)
        else:
            print("enter the valid options")
    elif(ch==3):
        kms=int(input("enter the distance covered:"))
        if(kms<=1):
            price=20
            print("the bill amount is",price)
        elif(kms<=4):
            rate=18
            price=kms*rate
            print("the bill amount is",price)
        elif(kms>4):
            rate=15
            price=kms*rate
            print("the bill amount is",price)
        else:
            print("enter the valid options")
    elif(ch==4):
        flg=False
    else:
        print("enter the valid options")

