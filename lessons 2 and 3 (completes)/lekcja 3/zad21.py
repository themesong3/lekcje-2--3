name = input("Your university name ")
l = []
for i in range(len(name)):
    l.append(name[i])
    l.append(" ")

for i in range(len(l)):
    print(l[i], end="")