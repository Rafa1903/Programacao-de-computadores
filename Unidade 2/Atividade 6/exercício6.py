"""
4. Faç•a um programa que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma.
Imprima na tela a matriz, a linha de maior soma e a soma.
"""
matriz = []
maior_soma = 0
maior_linha = 0
for i in range(3):
    linha = []
    soma_linha = 0
    for j in range(3):
        n = int(input("Digite um número: "))
        linha.append(n)
        soma_linha = soma_linha + n
    matriz.append(linha)
    if (soma_linha > maior_soma):
        maior_soma = soma_linha
        maior_linha = i
print(matriz)
print(matriz[maior_linha])
print(maior_soma)