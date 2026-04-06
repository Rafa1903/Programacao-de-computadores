"""
8. Leia um número e: Se for positivo, mostre a raiz aproximada (use **0.5); Caso contrário,
informe “Número inválido”
"""
n1 = float(input("Digite um número"))
if(n1 > 0):
    n2 = n1 ** 0.5
    print(n2)
else:
    print("Número inválido")