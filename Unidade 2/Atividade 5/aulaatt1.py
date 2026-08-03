"""
Escreva um programa que lê 7
valores inteiros, armazena-os em
uma lista e, em seguida, mostra os
valores lidos em ordem inversa à
leitura.
"""
lista = []

for i in range(7):
    n = int(input("Digite um número inteiro: "))
    lista.append(n)

print(lista[::-1])