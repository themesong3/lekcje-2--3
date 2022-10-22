x = int(input("X value "))
y = int(input("Y value "))
if x > 0 and y > 0:
    q = "first"
if x < 0 and y > 0:
    q = "second"
if x < 0 and y < 0:
    q = "third"
if x > 0 and y < 0:
    q = "fourth"
print(f"Your point is in the {q} quarter")
