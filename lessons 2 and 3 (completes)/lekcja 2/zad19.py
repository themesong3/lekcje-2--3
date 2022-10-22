heightCm = float(input("How tall are you (cm) ? "))
weight = float(input("Tell me your weight (kg) "))
bmi = weight / ((heightCm / 100)**2)
print(f"Your BMI is {bmi}\n")