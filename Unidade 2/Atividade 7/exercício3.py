"""
3) Faça um programa que lê 3 notas de um aluno no semestre, calcula sua
média a partir de uma função e informa se o aluno está aprovado (media >=
7) ou reprovado (media < 7).
"""
import funcoes

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))

media = funcoes.media(nota1,nota2,nota3)
print("A média deu: ",media)
if (media >= 7):
    print("Está aprovado")
else:
    print("Está reprovado")