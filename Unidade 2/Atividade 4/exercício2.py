
"""
2) Escreva um programa que leia um número inteiro positivo (n > 1)
e imprima o número de seus divisores.
"""

n = int(input("Digite um número: "))
contador = 0
for i in range(1, n + 1):
    if (n > 1):
        if (n % i == 0):
            print(i)
            contador = contador + 1
print(f"Tem {contador} divisores desse número")        
            

            