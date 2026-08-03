


arquivo = open("nomes.txt", "w")
for i in range(5):
    nomes = input("Digite o seu nome: ")
    arquivo.write(nomes + "\n")
arquivo.close()
