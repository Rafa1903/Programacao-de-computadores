"""
19. Leia dois números e: Verifique se são iguais ou diferentes. Sendo diferentes mostre a diferença
entre eles.
"""
n1 = int(input("Digite o primeiro número"))
n2 = int(input("Digite o segundo número"))
if(n1 != n2):
    if(n1 > n2):
        print("A diferença é", n1 - n2)
    else:
        print("A diferença é", n2 - n1)
else:
    print("São iguais")    