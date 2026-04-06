"""
10. Leia um número e informe: “Dentro do intervalo” se estiver entre 0 e 10; “Fora do intervalo”
caso contrário.
"""
n1 = float(input("Digite um número"))
if(n1 >= 0) and (n1 <= 10):
    print("Dentro do intervalo", n1)
else: 
    print("Fora do intervalo", n1)