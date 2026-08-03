# Exemplo
lista = []
n = int(input("Digite a quantidade de números: "))
for i in range(n):
    numero = int(input("Digite um número inteiro positivo: "))
    if (n >= 1):
        lista.append(numero)
x = int(input("Digite um número que desejo buscar: "))

if x in lista:
    print("O número")