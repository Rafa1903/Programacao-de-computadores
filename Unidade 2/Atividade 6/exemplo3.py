# Usando dicionários (delimitado por chaves)

dados_cliente = {
    "Nome": "Renan",
    "Endereço": "Rua Cruzeiro do Sul",
    "Telefone": "982503645" }
print(dados_cliente["Nome"]) # Renan
print(dados_cliente["Endereço"]) # Rua Cruzeiro di Sul
print(dados_cliente["Telefone"]) # 982503645

# Adicionando mais uma chave no dicionário
dados_cliente["Idade"] = 40
print(dados_cliente)
print(dados_cliente["Idade"]) # 40

# Apagando uma chave dentro do dicionário
dados_cliente.pop("Telefone", None)
print(dados_cliente)