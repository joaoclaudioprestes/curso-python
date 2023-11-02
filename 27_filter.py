# Filter é usado para filtrar algo
x = [12, 13, 14, 15, 25, 26, 27, 28, 30, 31, 32, 33]
y = [{'nome': 'joão', 'idade': 18}, {'nome': 'carlos', 'idade': 28}]

x = list(filter(lambda x: x < 18, x))
# Elementos menores que 18 foram adicionados em x

y = list(filter(lambda y: y['nome'] == 'carlos', y))

print(x)
print(y)