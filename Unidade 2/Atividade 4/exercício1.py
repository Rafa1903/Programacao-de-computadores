"""
1) Escreva um programa que leia um número inteiro positivo (n > 1)
e imprima os seus divisores.
"""

n = int(input("Digite um número: "))
for i in range(1, n + 1,):
    if (n > 1):
        if (n % i == 0):
            print(i)
print("Fim do programa")