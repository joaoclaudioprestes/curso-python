def minha_funcao():
    print('oie')
    print('Tudo bem?')

def soma_numeros(n1,n2,*args): #*args recebe paramentros pórem não define a quantidade
    print(f'n1 = {n1} n2 = {n2} *args = {args}')

    for i in args:
        soma = 0
        soma = soma + i
    print(soma)


def test_kwargs(teste = 1, teste1 = 2, teste3 = 3): #**kwargs empacota tudo em dicionarios
    print(teste, teste1, teste3)


def soma_valores(n1, n2):
    soma = n1 + n2

    return soma


soma = soma_valores(5,2)

print(soma)



# minha_funcao()

# soma_numeros(10,25,25,15,35,96)

# test_kwargs()
