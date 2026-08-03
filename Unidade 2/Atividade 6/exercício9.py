# 3. Faça um programa que verifique se uma palavra é um palíndromo (ex.: “arara”).

palavra = input("Digite uma palavra: ")
palavra_invertida = palavra[::-1]

if (palavra == palavra_invertida):
    print("É políndromo")
else:
    print("Não é políndromo")