"""
4) Faça um programa que leia dois números reais e um símbolo que identifique
uma operação matemática (+, -, *, /), submetendo-os para a função
calculadora (crie a função). A função deverá efetuar um cálculo entre os dois
números submetidos, baseado no símbolo digitado.
"""

import funcoes

num1 = float(input("Digite o primeiro número: "))
simbolo = input("Digite uma operação matemática(+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

calculadora = funcoes.calculadora(num1,simbolo,num2)
print("O resultado foi: ",calculadora)