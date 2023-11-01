print('x----- Maior Número -----x')

number_one = float(input('Digite o primeiro número: '))
number_two = float(input('Digite o segundo número: '))
number_tree = float(input('Digite o terceiro número: '))

if (number_one > number_two and number_one > number_tree):
    print(f'O maior número é {number_one}')
elif (number_two > number_one and number_two > number_tree):
    print(f'O maior número é {number_two}')
elif (number_tree > number_one and number_tree > number_two):
    print(f'O maior número é {number_tree}')