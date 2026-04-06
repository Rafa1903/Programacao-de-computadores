#4. Leia um número e informe se ele é par ou ímpar.

n1 = float(input("Digite um número"))
if(n1 % 2 == 0):
    print("É par", n1)
else:
    print("É ímpar", n1)