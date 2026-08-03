
import funcoes

#aula 02/06/2026
#Funções

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))

resultado = funcoes.soma(num1, num2)
print("Resultado da soma:", resultado)

resultado2 = funcoes.subtracao(num1,num2)
print("Resultado da subtração é: ", resultado2)

# Ao quadrado do primeiro input
resultado3 = funcoes.quadrado(num1)
print("Resultado ao quadrado dos valores é: ", resultado3)

# Colocando e mostrando uma variável no arquivo dados.txt
funcoes.manipulacao_arquivo(str(resultado))

"""
Depois separar direitinho cada "read"
"""
# Lendo o arquivo
arquivo = open("dados.txt", "r")
dados = arquivo.read()

# Divide o (livro) em partes para o sistema não acabe a memória
linha1 = arquivo.readline()
linha2 = arquivo.readline()

# Coloca as linhas em uma lista
linhas = arquivo.readlines()

for linha in linhas:
    print(linha)

print(linha1)
print(linha2)
print(dados)
arquivo.close()

