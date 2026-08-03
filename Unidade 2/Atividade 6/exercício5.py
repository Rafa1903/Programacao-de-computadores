"""
3. Faça um programa que leia as dimensões de duas matrizes A e B, e depois leia as duas
matrizes (os elementos devem ser inteiros). Se as matrizes forem de tamanhos compatíveis para
multiplicação, multiplique as matrizes. Imprima as matrizes A, B e a matriz resultante da
multiplicação
"""
a1 = int(input("Digite o número de linhas da matriz A: "))
a2 = int(input("Digite o número de colunas da matriz A: "))
matrizA = []
for i in range(a1):
    linhaA = []
    for j in range(a2):
        n1 = int(input("Digite um número inteiro: "))
        linhaA.append(n1)
    matrizA.append(linhaA)
print(matrizA)

b1 = int(input("Digite o número de linhas da matriz B: "))
b2 = int(input("Digite o número de colunas da matriz B: "))
matrizB = []
for i in range(b1):
    linhaB = []
    for j in range(b2):
        n2 = int(input("Digite um número inteiro: "))
        linhaB.append(n2)
    matrizB.append(linhaB)
print(matrizB)

if (a2 == b1):
    matrizC = []
    for i in range(a1):
        linhaC = []
        for j in range(b2):
            soma = 0
            for k in range(a2):
                soma = soma + (matrizA[i][k] * matrizB[k][j])
            linhaC.append(soma)
        matrizC.append(linhaC)
    print(matrizC)
else: 
    print("As matrizes não são compatíveis")

            