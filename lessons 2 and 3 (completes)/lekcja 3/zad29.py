numbers = []
while True:
    option = int(input("Give me a number" ))
    if option == 0:
        break
    else:
        numbers.append(option)

sum = 0
for i in range(len(numbers)):
    sum += numbers[i]

print(f"Suma: {sum} Ilosc: {len(numbers)} Średnia: {sum/len(numbers)}")
