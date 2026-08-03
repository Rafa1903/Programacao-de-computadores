# strip: Tira os espaços que atrapalham
frase = " oi mundo "
print(frase)
print(frase.strip())

# split(separador): Divide as substring com base a um separador
nomes = "Ana, João, Carlos"
print(nomes.split(","))

# Exercício
#Incompleto
vogais = "a", "e", "i", "o", "u"
palavra = input("Digite uma palvra: ")
if palavra.find(vogais):
    print("Há vogais")
else: 
    print("Não há vogais")