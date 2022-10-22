ageH = int(input("Enter the dog's age in human years "))
ageD = 0
counter = 0
while counter < ageH:
    if counter < 2:
        ageD += 10.5
        counter += 1
    else:
        ageD += 4
        counter += 1
print(f"The dog's age in dog’s years is {ageD}")