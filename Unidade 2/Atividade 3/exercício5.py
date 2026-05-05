"""
5. Peça números ao usuário continuamente e informe se cada número é par ou ímpar. O programa só
deve parar quando o usuário digitar 0.
"""

while True:
  n = int(input("Digite um número: "))
  if(n == 0):
    break
  elif (n % 2 ==  0):
    print("Par")
  else:
    print("Ímpar")
print("Fim do programa")
