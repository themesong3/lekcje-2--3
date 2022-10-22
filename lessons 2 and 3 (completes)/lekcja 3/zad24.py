dl = 0
for i in range(5):
    dl += 1
    for j in range(dl):
        print("*", end = "")
    print("")

dl = 5
for i in range(4):
    dl -= 1
    for j in range(dl):
        print("*", end = "")
    print("")   