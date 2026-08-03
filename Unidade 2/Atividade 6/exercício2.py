"""
Faça um programa que armazena os nomes e idades de 10 pessoas em uma
matriz, e imprime o nome da pessoa mais nova.
"""

matriz = []
menor_idade = 999
nome_menor = ""
for i in range(10):
    linha = []
    nome = input("Digite um nome: ")
    linha.append(nome)
    idade = int(input("Digite a sua idade: "))
    linha.append(idade)
    if (menor_idade > idade):
        menor_idade = idade
        nome_menor = nome 
    matriz.append(linha)
print(matriz)
print(f"O {nome_menor} tem {menor_idade} anos, logo é a pessoa que tem a menor idade")