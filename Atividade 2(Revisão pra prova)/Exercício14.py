"""
14. Leia um valor e: Converta para inteiro; Se for múltiplo de 3 → “Múltiplo de 3”; Senão → “Não é
múltiplo”.
"""
n1_str = input("Digite um valor")
n1 = int(n1_str)
if(n1 % 3 == 0):
    print("É múltiplo de 3", n1)
else:
    print("Não é múltiplo", n1)