# Exercício do slide 8
"""
1. Leia 10 números inteiros e armazene-os em uma lista. Ao final: mostre todos os valores, informe o maior
valor, informe o menor valor.
2. Receba 15 números inteiros e armazene-os em uma lista. Depois: crie uma lista apenas com números
pares, crie outra lista apenas com números ímpares, exiba as duas listas.
3. Leia 8 números inteiros e armazene-os em uma lista. Em seguida: solicite um número ao usuário,
informe se o número está ou não presente na lista.
4. Desenvolva um programa que: leia 10 números inteiros e os armazene em uma lista, solicite ao usuário um
número para remoção, remova todas as ocorrências desse número da lista, exiba a lista atualizada. Caso o
número não exista na lista, informe ao usuário.
5. Leia 20 números inteiros e armazene-os em uma lista. Depois: conte quantos números são positivos
conte quantos são negativos, conte quantos são iguais a zero.
6. Crie duas listas com 5 números cada. Depois: informe quais valores aparecem nas duas listas, informe
quais valores são exclusivos de cada lista.
7. Cadastre: nome, preço, quantidade em estoque de 5 produtos utilizando listas. Depois: mostre os
produtos com estoque menor que 10, informe o produto mais caro.
8. Crie um programa que: leia 12 números inteiros e armazene-os em uma lista, exiba os números em ordem
crescente, exiba os números em ordem decrescente, informe quantos números são pares e quantos são
ímpares
"""
while True:
    print("==========MENU==========")
    print("Algoritmo 1")
    print("Algoritmo 2")
    print("Algoritmo 3")
    print("Algoritmo 4")
    print("Algoritmo 5")
    print("Algoritmo 6")
    print("Algoritmo 7")
    print("Algoritmo 8")
    print("Sair : 9")
    
    algoritmo = int(input("Digite qual o algoritmo deverá ser: "))

    if (algoritmo == 1):
        lista = []
        for i in range(10):
            n = int(input("Digite um número inteiro: "))
            lista.append(n)
        menor = min(lista)
        maior = max(lista)
        print(lista)
        print(f"O menor valor da lista é {menor} e o maior é {maior}!!!")

    elif (algoritmo == 2):
        lista = []
        par = []
        impar = []
        for i in range(15):
            n = int(input("Digite um número inteiro: "))
            lista.append(n)
        for j in lista:
            if (j % 2 == 0):
                par.append(j)
            else:
                impar.append(j)
        print(par)
        print(impar)
    
    elif (algoritmo == 3):
        lista = []
        for i in range(8):
            n = int(input("Digite um número inteiro: "))
            lista.append(n)
        x = int(input("Digite um número para ver se ele está na lista: "))
        if x in lista:
            print(f"O número {x} está na lista.")
        else:
            print(f"O número {x} não está na lista.")
    
    elif (algoritmo == 4):
        lista = []
        for i in range(10):
            n = int(input("Digite um número inteiro: "))
            lista.append(n)

        x = int(input("Qual número devo retirar? "))
        r = lista.count(x)
        if x in lista:
            for i in range(r):
                lista.remove(x)
        else:
            print("Não tem esse número na lista.")
        print(lista)
    
    elif (algoritmo == 5):
        lista = []
        positivo = 0
        negativo = 0
        zero = 0
        for i in range(20):
            n = int(input("Digite um número inteiro: "))
            lista.append(n)
        for j in lista:
            if (j == 0):
                zero = zero + 1
            elif (j > 0):
                positivo = positivo + 1
            else:
                negativo = negativo + 1
        print(f"Tem {zero} números zeros, {positivo} números positivos e {negativo} números negativos.")
    
   
    elif (algoritmo == 6):
        lista1 = []
        lista2 = []
        exclusivo1 = []
        exclusivo2 = []
        for i in range(5):
            n = int(input("Digite um número inteiro: "))
            lista1.append(n)
        for i in range(5):
            n = int(input("Digite um número inteiro: "))
            lista2.append(n)
        for j in lista1:
            if j not in lista2:
                exclusivo1.append(j)
        for j in lista2:
            if j not in lista1:
                exclusivo2.append(j)
        print(f"Valores exclusivos da primeira lista: {exclusivo1}")
        print(f"Valores exclusivos da segunda lista: {exclusivo2}")

    elif (algoritmo == 7):
        nomes = []
        precos = []
        estoque = []
        for i in range(5):
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade em estoque: "))
            nomes.append(nome)
            precos.append(preco)
            estoque.append(quantidade)
        for i in range(5):
            if (estoque[i] < 10):
                print(nomes[i])
        maior = max(precos)
        indice = precos.index(maior)
        print(f"O produto mais caro é {nomes[indice]} e custa R${maior}")

    elif (algoritmo == 8):
        lista = []
        pares = 0
        impares = 0
        for i in range(12):
            n = int(input("Digite um número inteiro: "))
            lista.append(n)
        for j in lista:
            if (j % 2 == 0):
                pares = pares + 1
            else:
                impares = impares + 1
        print(f"Tem {pares} números pares e {impares} números impares.")
        print(sorted(lista))
        print(sorted(lista)[::-1])
    

    elif (algoritmo == 9):
        print("Programa encerrado")
        break

    else:
        print("Algoritmo inválido!")



