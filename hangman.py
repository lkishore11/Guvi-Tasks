import random
a=['cat','dad','mom','dog','mod','pen','pet']
flg=True
while(flg):
    print("Guess a word from:")
    print(a)
    A=random.choice(a)
    b=input()
    print ("You Lose The word is",A)
    if b in A and b!='':
        print("You Won")
        ex=input("enter q to exit or else try again")
        if(ex=='q' or ex=='Q'):
            flg=False
    else:
        print("You lose")
        ex=input("enter q to exit or else try again:")
        if(ex=='q' or ex=='Q'):
            flg=False
