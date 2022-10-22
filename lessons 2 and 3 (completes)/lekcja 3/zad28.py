pos1 = 0
pos2 = 1
print(pos1)
print(pos2)
for i in range(51):
    pos3 = pos2 + pos1
    print(pos3)
    pos1 = pos2
    pos2 = pos3
