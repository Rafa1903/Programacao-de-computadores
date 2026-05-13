"""
5) Escreva um programa que repita as seguintes etapas até que o
usuário digite a palavra "nao":
i. Leia a distância percorrida por um atleta (em Km);
ii. Leia o tempo gasto para percorrer essa distância (em horas);
iii. Calcule e exiba a velocidade média do atleta (velocidade = distância /
tempo);
iv. Pergunte ao usuário se deseja continuar utilizando o programa
(respostas possíveis: "sim" ou "nao").
"""

n = input("Poderia responder algumas questões? ")
while True:
    if(n == "nao"):
        break
    if (n == "sim"):
        distancia = float(input("Quantos km o atleta percorreu? "))
        tempo = float(input("Quantas horas o atleta demorou para percorrer essa distância? "))
        velocidade = distancia / tempo
        print(f"A velocidade foi de: {velocidade:2f} km/h")
        n = input("Quer continuar? ")
print("Fim do programa")


