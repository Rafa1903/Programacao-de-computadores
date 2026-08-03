"""
Faça um programa que leia uma matriz 3x3 de inteiros e multiplique os elementos da diagonal
principal da matriz por um número k. Imprima a matriz na tela antes e depois da multiplica•ção.
"""


k = int(input("Qual o valor de k: "))
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        n = int(input("Digite um número inteiro: "))
        linha.append(n)           
    matriz.append(linha)
print(matriz)

for i in range(3):
    for j in range(3):
        if (i == j):
            matriz[i][j] = matriz[i][j] * k
print(matriz)