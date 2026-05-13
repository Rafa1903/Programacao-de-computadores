

# Exercício
# incompleto
n = int(input("Digite um número que irá pra lista: "))
lista = []
while True:
    if (n < 0):
        break
    if (n > 0):
        lista.append(n)
        n = int(input("Digite um número diferente: "))
print(lista)