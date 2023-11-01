# Solicita ao usuário que digite um número e armazena-o em n1
n1 = int(input('Digite um número: '))

# Loop for para calcular a tabuada de n1 de 1 a 10
for i in range(1, 11):
    # Calcula o produto de n1 e i e armazena-o em mult
    mult = n1 * i
    # Imprime a expressão da multiplicação
    print(f'{n1} x {i} = {mult}')