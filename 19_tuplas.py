# Definindo uma tupla com informações de uma pessoa
pessoa = ("João", 25, "joao@email.com")

# Acessando elementos da tupla
nome = pessoa[0]  # O primeiro elemento (nome) está no índice 0
idade = pessoa[1]  # O segundo elemento (idade) está no índice 1
email = pessoa[2]  # O terceiro elemento (email) está no índice 2

# Imprimindo as informações da pessoa
print("Nome:", nome)
print("Idade:", idade)
print("Email:", email)

# Tentativa de modificar a tupla (Isso resultará em um erro)
# pessoa[1] = 26  # Isso causará um erro porque as tuplas são imutáveis

# Desempacotamento de tupla
nome, idade, email = pessoa  # Desempacotando a tupla em variáveis individuais

# Imprimindo as informações novamente após o desempacotamento
print("Nome após desempacotamento:", nome)
print("Idade após desempacotamento:", idade)
print("Email após desempacotamento:", email)
