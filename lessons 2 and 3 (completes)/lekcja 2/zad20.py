import random

print("Now lets roll some dice\n")
roll1 = random.randrange(1,7,1)
roll2 = random.randrange(1,7,1)
roll3 = random.randrange(1,7,1)
print(f"Roll 1 = {roll1}  Roll 2 = {roll2}  Roll 3 = {roll3}\n")
print(f"Their sum is {roll1 + roll2 + roll3}")