"""
Programa que lê uma matriz 3x3 digitada pelo usuário e conta
quantos números pares existem na matriz, imprimindo na tela o resultado e a
matriz.
"""

matriz = []
pares = 0
for i in range(3):
    linha = []
    for j in range(3):
        n = int(input("Digite números para formar uma matriz 3x3: "))
        linha.append(n)
        if (n % 2 == 0):
            pares = pares + 1
    matriz.append(linha)
print(matriz)
print(f"Essa matriz tem {pares} pares!")
