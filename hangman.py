import random
a=['cat','dad','mom','dog','mod','pen','pet']
for i in range(5):
    print("Guess a word from:")
    print(a)
    A=random.choice(a)
    b=i
        print ("You Lose The word is",A)nput()
    if b in A:
        print("You Won")
    else:
