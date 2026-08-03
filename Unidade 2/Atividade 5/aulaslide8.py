#Praticando/tentando fazer as atividades

"""
1) Escreva um programa que leia
números positivos e os armazene
numa lista (até que um número
não positivo seja fornecido). Por
fim, seu programa receberá um
número inteiro x e deve verificar se
x pertence ou não à lista
"""

n = int(input("Digite um número positivo: "))
lista = []

while True:
    if (n <= 0):
        break
    if (n > 0):
        lista.append(n)
        n = int(input("Digite outro número: "))
x = int(input("Qual número você quer verificar se pertence a lista? "))
if x in lista:
    print(f"O número {x} está na lista!")
else:
    print(f"O número {x} não pertence a lista!")
print(lista)
