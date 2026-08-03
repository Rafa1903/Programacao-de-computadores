# 8. Leia uma matriz 4x4 e informe qual é o maior número armazenado nela.
maior = 0
matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        n = int(input("Digite um número inteiro: "))
        linha.append(n)
        if (n > maior):
            maior = n
    matriz.append(linha)
print(matriz)
print(maior)