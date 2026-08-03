# 7. Crie uma matriz 3x3 com números inteiros e mostre a soma de todos os elementos
soma = 0
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        n = int(input("Digite um número inteiro: "))
        linha.append(n)
        soma = soma + n
    matriz.append(linha)
print(matriz)
print(soma)