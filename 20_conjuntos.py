# Criando um conjunto
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {3, 4, 5, 6, 7}

# Adicionando elementos a um conjunto (mutável)
conjunto_a.add(6)  # Adicionando o elemento 6 ao conjunto A

# Removendo elementos de um conjunto (mutável)
conjunto_b.remove(7)  # Removendo o elemento 7 do conjunto B

# União de conjuntos
uniao = conjunto_a.union(conjunto_b)  # União dos conjuntos A e B

# Interseção de conjuntos
intersecao = conjunto_a.intersection(conjunto_b)  # Interseção dos conjuntos A e B

# Diferença de conjuntos
diferenca = conjunto_a.difference(conjunto_b)  # Diferença entre os conjuntos A e B

# Verificar se um conjunto é um subconjunto de outro
e_subconjunto = conjunto_a.issubset(conjunto_b)  # Verificando se A é subconjunto de B

# Imprimir os resultados
print("Conjunto A:", conjunto_a)
print("Conjunto B:", conjunto_b)
print("União:", uniao)
print("Interseção:", intersecao)
print("Diferença:", diferenca)
print("A é subconjunto de B:", e_subconjunto)
