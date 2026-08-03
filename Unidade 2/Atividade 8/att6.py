
arquivo = open("notas.txt", "r")

lista = []
soma = 0

for linha in arquivo:
    nota = float(linha.strip())
    lista.append(nota)
    soma =  soma + nota

arquivo.close()

quantidade = len(lista)
maior = max(lista)
menor = min(lista)
media = soma / quantidade

print("Quantidade de notas:", quantidade)
print("Maior nota:", maior)
print("Menor nota:", menor)
print("Média:", media)