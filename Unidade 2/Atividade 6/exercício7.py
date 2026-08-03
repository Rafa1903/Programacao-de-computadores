# 1. Crie um programa que receba uma palavra e mostre quantas vogais existem nela.
palavra = input("Digite uma palavra: ")
vogais = ["a", "e", "i", "o", "u"]
n_vogais = 0
for letras in palavra:
    if letras in vogais:
        n_vogais = n_vogais + 1
print(n_vogais)