#15. Leia um número e: Se estiver entre 10 e 20 → “Dentro”; Caso contrário → “Fora”.
n1 = float(input("Digite um número "))
if(n1 <= 20) and (n1 >= 10):
    print("Dentro", n1)
else:
    print("Fora", n1)