# 6. Peça vários números ao usuário (encerra com 0) e informe qual foi o maior número digitado.

maior = 0
while True:
    n = int(input("Digite um número: "))
    if (n == 0):
        break
    if (n > maior):
        maior = n
        
print("Fim do programa, o maior número foi: ", maior) 