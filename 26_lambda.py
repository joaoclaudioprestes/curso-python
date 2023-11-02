import os
# Lambda ela e mais curta e sempre retorna algo e não necessariamente precisamos declar a função antes

x = lambda nome, idade: print(f'Nome: {nome}\nIdade: {idade}')
y = lambda: 10 + 25

x('João', 18)
print(y)
