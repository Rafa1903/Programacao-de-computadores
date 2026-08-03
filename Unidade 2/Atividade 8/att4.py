soma_elementos = 0
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        n = int(input("Digite um número inteiro: "))
        linha.append(n)
        soma_elementos = soma_elementos + n
    matriz.append(linha)
print("Elementos",soma_elementos)

soma_diagonalP = 0
for i in range(3):
    for j in range(3):
        if (i == j):
            soma_diagonalP = soma_diagonalP + matriz[i][j] 
print("Diagonal principal: ", soma_diagonalP)
print(matriz)
