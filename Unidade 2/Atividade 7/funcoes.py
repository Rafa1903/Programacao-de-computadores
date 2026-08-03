# transferindo a função para outro arquivo (main)

def soma(a,b):
    return a + b

def subtracao(a, b):
    return a - b

def quadrado(a):
    return a ** 2


def manipulacao_arquivo(texto):
    arquivo = open("dados.txt", "w")
    arquivo.write(texto)

# Exercício 2
def perimetro_retangulo(x,y):
    return (2*x) + (2*y)

# Exercício 3
def media(x,y,z):
    return (x + y + z) / 3

# Exercício 4
def calculadora(x,y,z):
    if (y == "+"):
        return x + z
    elif (y == "-"):
        return x - z
    elif (y == "*"):
        return x * z
    elif (y == "/"):
        if (z == 0):
            print("Não pode dividir um número por 0")
        else:
            return x / z
    else:
        return "Operação inválida"
    

# Exercício 5
# 1
def media1(a,b):
    return (a + b) / 2

# 2
def diferenca(a,b):
    if (a > b):
        return a - b
    else:
        return b - a

# 3
def multiplicacao(a,b):
    return a * b

# 4
def divisao(a,b):
    if (b == 0):
        print("Não pode dividir qualquer número por 0")
    else:
        return a / b