#17. Leia idade e: Mostre: Menor de idade (<18); Adulto (18 a 59); Idoso (60+).
n1 = int(input("Qual é a sua idade?"))
if(n1 < 18):
    print("Menor de idade", n1)
elif(n1 >= 18) and (n1 <= 59):
    print("Adulto", n1)
else:
    print("Idoso", n1)