"""
7) Agenda telefônica (Listagem) - Faça um programa que:
 Receba o nome do arquivo a ser lido;
 Leia o arquivo indicado pelo usuário (a partir do nome do arquivo);
 Exiba o nome e o telefone cadastrados no mesmo.
"""
nome_arquivo = input("Digite o nome do arquivo que quer ler: ")
arquivo = open(nome_arquivo, "r")
print(arquivo.read())
