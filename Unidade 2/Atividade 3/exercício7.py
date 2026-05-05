# 7. Peça várias notas ao usuário (encerra quando digitar -1) e calcule a média das notas válidas.

quantidade_notas = 0
soma_notas = 0
while True:
    nota = float(input("Digite as suas notas: "))
    if (nota == -1):
        break
    else:
        soma_notas = soma_notas + nota
        quantidade_notas = quantidade_notas + 1
        media = (soma_notas / quantidade_notas)
print("Fim do programa, a média das notas foi de: ", media)