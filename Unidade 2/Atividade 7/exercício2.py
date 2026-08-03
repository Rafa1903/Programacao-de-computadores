"""
2) Faça um programa que lê os lados de um retângulo e calcula o seu
perímetro a partir de uma função:
 Perímetro do retângulo = (2*largura) + (2*comprimento)
"""

import funcoes

lado1 = float(input("Digite a largura do retângulo: "))
lado2 = float(input("Digite o comprimento do retângulo: "))

resultado = funcoes.perimetro_retangulo(lado1,lado2)
print("O perímetro do retângulo vai ser: ", resultado)