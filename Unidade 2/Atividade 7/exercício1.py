"""
Faça um programa que permita ao usuário verificar se uma senha a ser
cadastrada em um sistema é válida ou não. O sistema em questão tem os
seguintes critérios para validar uma senha:
 Deve ter 6 caracteres (nem mais nem menos);
 Deve ter letras e números;
 Não deve constar as palavras ‘FLA’, ‘MENGO’ ou ‘MENGAO’
 Não deve começar com a letra ‘A’ nem terminar com a letra ‘F’
"""

senha = input("Digite uma senha de 6 dígitos: ")
senha_valida = True
tem_letra = False
tem_numero = False

if (len(senha) == 6):
    print("Primeiro requisito satisfeito")
else:
    print("Não satisfaz")
    senha_valida = False

for caractere in senha:
    if caractere.isalpha():
        tem_letra = True
    if caractere.isdigit():
        tem_numero = True

if tem_letra and tem_numero:
    print("Possui letras e números")
else:
    print("Precisa ter letras e números")
    senha_valida = False

if "FLA" in senha:
    print("Senha inválida, palavra proibida (FLA)")
    senha_valida = False
if "MENGO" in senha:
    print("Senha inválida, palavra proibida (MENGO)")
    senha_valida = False
if "MENGAO" in senha:
    print("Senha inválida, palavra proibida (MENGAO)")
    senha_valida = False

if senha.startswith("A"):
    print("Senha inválida, não pode começar com (A)")
    senha_valida = False
if senha.endswith("F"):
    print("Senha inválida, não pode terminar com (F)")
    senha_valida = False

if senha_valida:
    print("Senha válida")
else:
    print("Senha inválida")

