"""
11. Leia um número e: Se for par e positivo → “Par positivo”; Se for par e negativo → “Par
negativo”; Caso contrário → “Ímpar”.
"""
n1 = int(input("Digite um número"))
if(n1 > 0) and (n1 % 2 == 0):
    print("Par positivo", n1)
elif(n1 < 0) and (n1 % 2 == 0):
    print("Par negativo", n1)
else:
    print("Ímpar")