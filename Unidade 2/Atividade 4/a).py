# Somar todos os valores dessa lista e depois imprimi o resultado
numeros = [3, 7, 12, 18, 5, 9, 15]
soma = numeros[0]
for i in numeros:
    soma = soma + i
print("Deu:",soma)

# Testando o comando range ( de 1 a 100)

for i in range(1,101):
    print(i)
print("Fim do programa")

# Imprimindo de 1 até n (usando range)
n = int(input("Digite um número: "))
for i in range(1, n+1):
    print(i)
print("Fim do programa")

# Potencia de 2
n = int(input("Digite um número: "))
potencia = 1
for i in range(1, n+1):
    potencia = potencia * 2
print(potencia)