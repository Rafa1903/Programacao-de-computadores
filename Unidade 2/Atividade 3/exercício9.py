"""
9. Peça números ao usuário até que ele digite 0. Ao final, informe quantos números positivos e quantos
negativos foram digitados.
"""

quanti_posi = 0
quanti_nega = 0
while True:
    n = float(input("Digite um número: "))
    if (n == 0):
        break
    if (n > 0):
        quanti_posi = quanti_posi + 1
    else:
        quanti_nega =  quanti_nega + 1
print(f"Fim do programa, teve {quanti_posi} de números positivos e {quanti_nega} de números negativos")