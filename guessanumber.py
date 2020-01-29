import random
a=random.randint(1,100)
b=int(input("Guess a number between 1-100:"))
if a==b:
    print ("You Won")
else:
    print ("You Lose number is ",a)
