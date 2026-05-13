"""
4) Cada espectador de um cinema respondeu a um questionário com
a seguinte pergunta: Qual a sua opinião sobre o filme?
As opções de resposta foram: 3 – Ótimo, 2 – Bom e 1 – Regular
Escreva um programa que leia as respostas de 15 espectadores e
informe:
 A quantidade de pessoas que responderam "Ótimo";
 A quantidade de pessoas que responderam "Bom";
 A quantidade de pessoas que responderam "Regular".
"""


otimo = 0
bom = 0
regular = 0

# Esse range vai limitar a quantidade de respostas
for i in range(1, 16):
    respostas = int(input("Digite a sua avaliação: "))
    if (respostas == 1):
        regular = regular + 1
    if (respostas == 2):
        bom = bom + 1
    if (respostas == 3):
        otimo = otimo + 1
        
print(f"""Fim do programa, os espectadores deram {regular} notas regulares, 
      {bom} notas boas e {otimo} notas ótimas. """)