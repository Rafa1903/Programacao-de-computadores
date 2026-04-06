#13. Leia um número e: Se for maior que 100 → mostre metade; Senão → mostre o dobro.
n1 = int(input("Digite um número"))
if(n1 > 100):
    n2 = n1 * 0.5
    print("A metade é",n2)
else:
    n2 = n1 * 2
    print("O dobro é", n2)