ammount = int(input("How much money do you have "))
il5 = ammount//5
ammount -= il5*5

il2 = ammount//2
ammount -= il2*2

il1 = ammount//1
ammount -= il1*1

print(f"5 zl - {il5}\n2 zl - {il2}\n1 zl - {il1}")