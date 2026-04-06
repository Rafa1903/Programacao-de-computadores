#12. Leia dois números e: Mostre a soma; Mostre qual é maior ou se são iguais.
n1 = int(input("Digite o primeiro número"))
n2 = int(input("Digite o segundo número"))
n3 = n1 + n2
if(n1 > n2):
    print("O n1 é maior que n2 e a soma dos dois é", n3)
elif(n1 == n2):
    print("Os dois são iguais e a soma de ambos é", n3)
else:
    print("O n2 é maior que n1 e a soma dos dois é", n3)