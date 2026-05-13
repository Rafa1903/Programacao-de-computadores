"""
3) Escreva um programa que leia diversos números inteiros
positivos e exiba o dobro de cada um. A leitura deve ser
interrompida quando for digitado um número negativo.
"""

n = int(input("Digite um número: "))
while True:
    if(n < 0):
        break
    else:
        n = n * 2
        print(n)
        n = int(input("Digite um número novamente: "))
print("Fim do programa")