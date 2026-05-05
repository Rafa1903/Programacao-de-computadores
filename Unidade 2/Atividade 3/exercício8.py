# 8. Peça um número e mostre a tabuada dele de 1 a 10.

vezes = 1
n = int(input("Digite um número: "))
while True:
    if (vezes > 10):
        break
    if (vezes <= 10):
        print(f"{n} x {vezes} = ",n * vezes)
        vezes = vezes + 1
print("Fim do programa")