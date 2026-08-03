# 6. Crie uma matriz 3x3 preenchida pelo usuário e exiba todos os valores na tela.
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        n = int(input("Digite um número: "))
        linha.append(n)
    matriz.append(linha)
print(matriz)