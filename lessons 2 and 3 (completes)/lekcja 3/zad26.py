tries = 0
while tries < 3:
    tries += 1
    pin = input("Please enter PIN ")
    if pin == "0805":
        print("Correct !")
        break
    else:
        print("Wrong PIN\n")
        continue
if tries == 3:
    print("Sorry, your payment card has been blocked.")