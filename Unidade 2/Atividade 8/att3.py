
pares = 0
lista = []
for i in range(8):
    n = int(input("Digite um número inteiro: "))
    lista.append(n)
    if (n % 2 == 0):
        pares = pares + 1
    maior = max(lista)
    menor = min(lista)
print(f"A {pares} pares.")
print(f"O maior é {maior}")
print(f"O menor é {menor}")
print(lista)

