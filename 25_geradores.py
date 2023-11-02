def gerar_numeros(n):
    for i in range(n):
        yield i

# Utilizando o gerador para produzir números de 0 a 4
meu_gerador = gerar_numeros(5)

# Iterando e exibindo os valores produzidos pelo gerador
for numero in meu_gerador:
    print(numero)
