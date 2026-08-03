#Exemplo para quando a números repetidos

n = int(input("Digite uma dimensão/linhas para n da matriz: "))
m = int(input("Digite uma dimensão/colunas para m da matriz: "))
matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(0)
    matriz.append(linha)
print(matriz)