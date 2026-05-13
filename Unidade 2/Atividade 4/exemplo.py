# Encontre o maior valor dessa lista usando o while
numeros = [3, 1, 7, 9, 4]
i = 0
maior = numeros[0]

while (i < len(numeros)):
    if (numeros[i] > maior):
        maior = numeros[i]
    i = i + 1
print("O maior é:", maior)