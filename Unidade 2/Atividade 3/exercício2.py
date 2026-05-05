"""
2. Peça ao usuário para digitar uma senha. Continue solicitando até que ele acerte a senha correta
(defina uma senha fixa no código).
"""

n = int(input("Digite a senha:"))
senha = 12345
while (n != senha):
    print("Senha incorreta")
    n = int(input("Digite novamente: "))
print("Senha correta.")