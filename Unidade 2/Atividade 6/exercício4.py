"""
2. Faça um programa que leia duas matrizes A e B 2x2 de inteiros e imprima a matriz C que é a
soma das matrizes A e B.
"""
matrizA = []
for i in range(2):
    linhaA = []
    for j in range(2):
        a = int(input("Digite um número inteiro da matriz A: "))
        linhaA.append(a)
    matrizA.append(linhaA)
print(matrizA)

matrizB = []
for i in range(2):
    linhaB = []
    for j in range(2):
        b = int(input("Digite um número inteiro da matriz B: "))
        linhaB.append(b)
    matrizB.append(linhaB)
print(matrizB)

matrizC = []
for i in range(2):
    linhaC = []
    for j in range(2):
        c = matrizA[i][j] + matrizB[i][j]
        linhaC.append(c)
    matrizC.append(linhaC)
print(matrizC)
