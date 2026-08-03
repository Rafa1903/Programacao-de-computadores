# Verificar o tipo de dados 

#Incompleto (não sei o que escrever para printar o do isalnum)
while True:
    dados = input("Digite qualquer coisa: ")
    if (dados == -1):
        print("Programa encerrado")
        break
    elif dados.isdigit():
        print("Existem apenas números")
        
    elif dados.isalpha():
        print("Existem apenas letras")

    elif dados.isalnum():
        print("Existem letras e números")
        