"""
5) Faça um programa que receba dois
números e execute as operações listadas
a seguir, de acordo com a escolha do
usuário (crie uma função para cada opção).
(TEM UMA LISTA CERTA PARA CADA COMANDO)
"""
import funcoes

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

escolha = input("Escolha uma dessas opções: \n 1 - Média \n 2 - Diferença \n 3 - Multiplicação \n 4 - Divisão \n " \
"Escolha: ")

if (escolha == "1"):
    media = funcoes.media1(num1,num2)
    print("A média deu", media)

elif (escolha == "2"):
    dif = funcoes.diferenca(num1,num2)
    print("A diferença deu", dif)

elif (escolha == "3"):
    multi = funcoes.multiplicacao(num1,num2)
    print("A multiplicação deu", multi)

elif (escolha == "4"):
    div = funcoes.divisao(num1,num2)
    print("A divisão é de", div)
    
else:
    print("Deu problema")