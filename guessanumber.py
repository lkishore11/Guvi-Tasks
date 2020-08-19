import random
f=True
while(f==True):
    a=random.randint(1,10)
    b=int(input("Guess a number between 1-10:"))
    if a==b:
        print ("You Won")
    else:
        print ("You Lose number is ",a)
    i=input('enter anything to continue:')
    if i=='n':
        f=False
    else:
        f=True
        continue