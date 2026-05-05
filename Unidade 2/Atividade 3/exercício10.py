"""
10. Defina um número fixo no código. Peça ao usuário para adivinhar até acertar. Informe se o palpite é
maior ou menor que o número correto.
"""
senha = 67
while True:
    n = int(input("Dê um palpite: "))
    if (n == senha):
        print("Parabéns, você acertou!!!")
        break
    if (n > senha):
        print("o palpite está maior que o número correto")
    else:
        print("O palpite está menor que o número correto")
print("Fim do programa")