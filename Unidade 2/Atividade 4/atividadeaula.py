

vingadores = ["Homem de Ferro", "Capitão América", "Thor", "Hulk", "Viúva Negra", "Gavião Arqueiro"]

vingadores.append("Homem Aranha")
if "Thor" in vingadores:
    print(vingadores.index("Thor"))

if "Viúva Negra" and "Homem de Ferro" in vingadores:
    vingadores.remove("Viúva Negra")
    vingadores.remove("Homem de Ferro")
    print(vingadores)


# Exercício
n = int(input("Digite um número que irá pra lista: "))
lista = []
while True:
    if (n < 0):
        break
    if (n > 0):
        lista.append(n)
        n = int("Digite um número diferente: ")


