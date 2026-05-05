"""
20. Leia um valor e: verifique se eles está entre 0 e 100, caso o número esteja fora do intervalo,
mostre na tela o valor.
"""
n1 = int(input("Digite um valor "))
if(n1 > 100) or (n1 < 0):
     print("Fora do intervalo", n1)
else:
    print("Fim do programa")