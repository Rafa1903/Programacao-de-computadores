"""
Escreva um programa que
leia 30 valores inteiros
positivos e armazene-os
em uma lista, e calcule e
imprima:
a) O menor valor da lista.
b) A quantidade de
elementos da lista que
são divisíveis pelo menor
valor.
"""

lista = []
contador = 0

for i in range(30):
    n = int(input("Digite um número inteiro positivo: "))
    lista.append(n)

menor = min(lista)
print(menor)

for j in lista:
    if (j % menor == 0):
        contador = contador + 1

print(lista)
print(f"O menor valor da lista é {menor}")
print(f"A quantidade de números divisíveis por {menor} é {contador}")