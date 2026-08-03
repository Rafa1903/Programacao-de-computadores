
nota = float(input("Qual o nota do aluno? "))
if (nota >= 0) and (nota <= 10):
    if (nota >= 7):
        print("Aprovado")
    elif (nota >= 5) and (nota <= 6.9):
        print("Recuperação")
    elif (nota < 5):
        print("Reprovado")  
else:
    print("Mandou a nota errada, tente novamente!")