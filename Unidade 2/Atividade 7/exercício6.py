"""
6) Agenda telefônica (Cadastro) - Faça um programa que:
 Receba o nome e o telefone de 3 pessoas;
 Receba o nome do arquivo a ser criado;
 Crie um arquivo (com o nome do arquivo indicado pelo usuário) para cada
pessoa e escreva o nome e o telefone no mesmo;
 O nome deverá ficar na primeira linha do arquivo;
 O telefone deverá ficar na segunda linha do arquivo;
"""
nome_arquivo1 = input("Digite o nome do arquivo: ")
arquivo1 = open(nome_arquivo1, "w")
nome = input("Digite o seu nome: ")
telefone = int(input("Digite o seu número de telefone: "))
arquivo1.write(nome + "\n" + str(telefone) + "\n")
arquivo1.close()

nome_arquivo2 = input("Digite o nome do arquivo: ")
arquivo2 = open(nome_arquivo2, "w")
nome = input("Digite o seu nome: ")
telefone = int(input("Digite o seu número de telefone: "))
arquivo2.write(nome + "\n" + str(telefone) + "\n")
arquivo2.close()

nome_arquivo3 = input("Digite o nome do arquivo: ")
arquivo3 = open(nome_arquivo3, "w")
nome = input("Digite o seu nome: ")
telefone = int(input("Digite o seu número de telefone: "))
arquivo3.write(nome + "\n" + str(telefone) + "\n")
arquivo3.close()
