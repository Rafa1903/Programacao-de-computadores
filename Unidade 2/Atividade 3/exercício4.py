"""
4. Peça números ao usuário e some-os. O programa deve parar quando o usuário digitar um número
negativo. Ao final, mostre a soma total.
"""
n1 = 0
while True:
  n = int(input("Digite um número: "))
  if (n < 0):
    break
  n1 = n1 + n
print("Fim do programa, o resultado foi", n1)


