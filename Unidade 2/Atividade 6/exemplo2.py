# Usando tuplas (Uma lista que nunca pode ser modificada/alterada)

aluno = ("Maria", 8.5, "Aprovado")
print("Nome:", aluno[0])
print("Nota:", aluno[1])
print("Situação:",aluno[2])

numero = (5,)
print(type(numero))

# Dá erro justamente por que não é possível alterar uma tupla(lista)
vogais = ("a", "e", "i", "o", "u")
vogais[1] = "E"