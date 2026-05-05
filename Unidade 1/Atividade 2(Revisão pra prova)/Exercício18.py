"""
18. Leia um número e: Mostre se ele é par positivo, par negativo, impar positivo, impar negativo ou
neutro.
"""
n1 = int(input("Digite um número"))
if(n1 > 0) and (n1 % 2 == 0):
    print("Par positivo", n1)
elif(n1 < 0) and (n1 % 2 == 0):
    print("Par negativo", n1)
elif(n1 > 0) and (n1 % 2 != 0):
    print("Ímpar positivo")
elif(n1 < 0) and (n1 % 2 != 0):
    print("Ímpar negativo")
else:
    print("Neutro")