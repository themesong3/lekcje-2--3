def list_to_string(l):
    s = ""
    for i in range(len(l)):
        s += l[i]
    return s


h = int(input("Height: "))
w = int(input("Width: "))

for i in range(h):
    line = [" "]*w
    if i == 0 or i == h-1:
        for k in range(w):
            line[k] = "*"
        print(list_to_string(line))
    else:
        line[0] = "*"
        line[w-1] = "*"
        print(list_to_string(line))


            