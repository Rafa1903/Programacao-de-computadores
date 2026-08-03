# exercício
# Incompleto

lista = []
contador = 0
for i in range(5):
    numero = int(input("Digite um número inteiro positivo: "))
    if (numero > 0):
        lista.append(numero)

menor = min(lista)

for j in lista:
    if (menor % j == 0):
        contador = contador + 1

print(f"O menor valor da lista é: {menor} e a quantidade de números divisíveis são {contador}")
