"""
Atividade de casa: 
Slide pág 67(caderno), 68(git_hub) e 74(completamento no caderno)
"""
#Exercício slide 4, pág 67
y = 2
condicao1 = ((4* (y**2)) + ((3*y) - 5)) >= 0
condicao2 = ((2*y) > 3) or ((y - 1) < 0)
print("A condição 1 é", condicao1)
print("A condição 2 é", condicao2)
"""
Exercício do slide 4, pág 68
1. Agora que você subiu de nível, desenvolva os seguintes algoritmos:
a) Elabore um algoritmo que receba dois números, calcule a multiplicação entre eles e apresente o
resultado.
b) Desenvolva um algoritmo que receba cinco números, calcule a média aritmética e apresente o
resultado final.
c) Construa um algoritmo que receba o valor de um produto e calcule o preço final considerando um
acréscimo de 8% de imposto.
d) Elabore um algoritmo que receba dois números e apresente o resultado da subtração entre eles.
e) Construa um algoritmo que receba a altura e o peso de uma pessoa e calcule o Índice de Massa
Corporal (IMC).
f) Elabore um algoritmo que receba a temperatura em graus Celsius e apresente o valor convertido
para graus Fahrenheit.
g) Construa um algoritmo que receba a quantidade de horas trabalhadas por um funcionário e o valor
da hora trabalhada, calculando o salário total.
"""
# a)
n_1 = float(input("Número um"))
n_2 = float(input("Número dois"))
n_3 = n_1 * n_2
print("O resultado da multiplicação foi", n_3)

# b)
nota_1 = float(input("Qual é a sua primeira nota"))
nota_2 = float(input("Qual é a sua segunda nota"))
nota_3 = float(input("Qual é a sua terceira nota"))
nota_4 = float(input("Qual é a sua quarta nota"))
nota_5 = float(input("Qual é a sua quinta nota"))
media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5)/5
print("A média aritmétrica foi", media)

# c)
produto = float(input("O valor do produto"))
pf = produto * 1.08
print("o prduto final deu", pf)

# d)
n1 = float(input("Qual é o primeiro número?"))
n2 = float(input("Qual vai ser o segundo número?"))
n3 = n1 - n2
print("A subtração entre os outros números, deu", n3)

# e)
peso = float(input("Qual é o seu peso?(Em kg)"))
altura = float(input("Qual é a sua altura?(Em m)"))
imc = peso / (altura * altura)
print(f"O seu imc deu {imc:.2f}.")

# f)
graus = float(input("Quanto está a temperatura agora?"))
fahrenheit = (graus * 1.8) + 32
print("Em fahrenheit, vai ser", fahrenheit)

# g)
horas = int(input("Trabalhou quantas horas nesse mês?"))
valor_hora = 10
salario_total = horas * valor_hora
print("O salário total vai ser", salario_total)
# Oi