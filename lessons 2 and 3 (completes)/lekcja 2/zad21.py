import random

print("Guessing game, I will role a dice and you try to guess what I got")
guess = int(input("What is your guess ? "))
rollGame = random.randrange(1,7,1)
if rollGame == guess:
    print("True")
else:
    print("False")