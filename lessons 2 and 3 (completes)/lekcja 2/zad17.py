heightCm = float(input("How tall are you (cm) ? "))
heightFeet = float(heightCm // 30.48)
heightInch = float((heightCm - (heightFeet * 30.48)) // 2.54)
print(f"You are roughly {heightFeet} feet and {heightInch} inches tall\n")
