# aula 12/05/2026

# Laços alinhados
# Tabuada do 1 a 10
for i in range(1,11):
    print("Tabuada do", i)
    for j in range(1,11):
        print( i, "x", j, "=", i * j)


# Troca um elemento por outro na lista
empresas = ["Apple", "Samsung", "LG", "Facebook"]
empresas[2] = "Google"
print(empresas)

# Usando o append (adiciona um elemento no último lugar da lista)
empresas.append("Microsoft")
print(empresas)

# Usando insert (implementa um elemento no local selecionado)
empresas.insert(2, "Xiaomi")
print(empresas)

# Usando index (ver qual é a numeração de tal elemento da lista)
if "Samsung" in empresas:
    print(empresas.index("Samsung"))
else:
    print("Não há")

# Usando o remove (Remove o item na lista)
print(empresas.remove("Apple"))
print(empresas)

# Usando o pop (remove um elemento especícifo da lista usando a numeração do elemento)
print(empresas.pop(4))
print(empresas)

# Usando count (Conta a quantidade de elementos iguais)
print(empresas.count("Xiaomi"))
print(empresas)

# Removendo elementos
n = int(input("Quantos números serão lidos? "))

lista = []
for i in range(n):
    lista.append(int(input()))

x = int(input("Qual o número deve ser removido? "))
c = lista.count(x)

for i in range(c):
    lista.remove(x)
print(lista)

# usando o reverse (apenas deixa a lista ao contrário)
empresas.reverse()
print(empresas)

# Usando sort (Deixa na ordem crescente os números)
a = [1, 5, 2, 4, 3]
print(sorted(a))

# Funções de mínimo, máximo e soma
print(min(a))
print(max(a))
print(sum(a))