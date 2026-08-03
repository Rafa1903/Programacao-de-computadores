# 4. Receba uma frase e substitua todas as ocorrências de uma palavra específica por outra.
frase = input("Digite uma frase: ")
palavra_antiga = input("Palavra Antiga: ")
palavra_nova = input("Palavra Nova: ")
if palavra_antiga in frase:
    frase1 = frase.replace(palavra_antiga, palavra_nova)
print(frase1)