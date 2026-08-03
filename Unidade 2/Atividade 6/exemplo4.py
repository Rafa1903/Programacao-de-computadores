# Métodos de strings

nome = "Raul Andrade"

# Se começar com ... faça isso...
if nome.startswith("Raul"):
    print("O nome começa com Raul")
elif nome.startswith("Afonso"):
    print("O nome começa com Afonso")

# Se terminar com... faça isso...
if nome.endswith("Andrade"):
    print("O nome termina com Andrade")
elif nome.endswith("Olivreira"):
    print("O nome termina com Oliveira")

# Deixar um texto(string) em letra minúscula
nome = "JOÃO RAFAEL"
nome_minusculo = nome.lower()
print(nome_minusculo)

# Deixar um texto(string) em letra maiúscula
nome = "joão rafael"
nome_maiuscula = nome.upper()
print(nome_maiuscula)

# Encontrar um sub string numa string(Se não encontrar/localizar a posição da palavra, imprima (-1))
frase = "Em um mundo repleto de escolhas, escolha jogar"

posicao = frase.find("jogar")
posicao1 = frase.find("escolha")
posicao2 = frase.find("Rafael")
print(posicao)
print(posicao1)
print(posicao2)

if (posicao2 != -1):
    print(posicao)
else:
    print("Palavra não localizada")

# Substituir um conjunto de caracteres de strinf para o outro
frase = "Flamengo campeão de 87"
correto = frase.replace("Flamengo", "Sport")

print(correto)

