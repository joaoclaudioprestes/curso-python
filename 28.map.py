x = [i for i in range(12, 26)]
y = [{'nome': 'joão', 'idade': 18}, {'nome': 'carlos', 'idade': 28}]

x = list(map(lambda x: 10 if x < 18 else(x), x))
y = list(map(lambda x: {'nome': ['nome'], 'idade': 'menor de 18 anos'} if y['idade'] < 38 else(x), x))

print(y)
print(x)