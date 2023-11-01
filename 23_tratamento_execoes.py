#O tratamento de exceções e usado para realizar verificações

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

try:# irá tentar
    print(n1/n2)
except:# será a exceção caso o código em try não rode...
    print('Não consegui efetuar o seu calculo!')
finally:# sempre será executado
    print('Programa Finalizado')

try:
    x = int(input('Digite um número: '))
    print(5/x)
except ValueError: #se retornar um erro
    print('Digite um número inteiro!')
except ZeroDivisionError: #erro nao por dividir por zero
    print('Digite um número diferente de zero!')

try:
    y = int(input('Digite um número: '))
    print(5/y)
except Exception as e:
    print('erro interno no sistema')
