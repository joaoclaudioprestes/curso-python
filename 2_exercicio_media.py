print('x----- Média -----x')

number_one = float(input('Digite o primeiro número: '))
number_two = float(input('Digite o segundo número: '))
number_tree = float(input('Digite o terceiro número: '))
number_for = float(input('Digite o quarto número: '))

media = (number_one + number_two + number_tree + number_for) / 4

if(media >= 6):
    result = ' aluno aprovado!'
elif(media >= 4):
    result = ' aluno está de recuperação'
else:
    result = ' aluno reprovou'

print(f'A média do aluno é {media}. O {result}')