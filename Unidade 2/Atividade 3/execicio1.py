# 1. Solicite uma nota entre 0 e 10. Continue pedindo até que o usuário informe um valor válido.

nota = float(input("Digite um número entre 0 e 10: "))

while (nota < 0) or (nota > 10):
    print("Nota inválida")
    nota = float(input("Digite novamente "))
print("Nota válida", nota)