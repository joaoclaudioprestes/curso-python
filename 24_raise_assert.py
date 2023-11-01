# raise 'Deu merda' #Chama uma excessão

# raise ValueError('Deu merda2')


def soma(n1,n2):
    if n1 < 0 or n2 < 0:
        raise ValueError('n1 e n2 não podem ser negativos') #O comando raise é usado para levantar (lançar) uma exceção em Python. Ele permite que você indique explicitamente que ocorreu um erro ou uma condição excepcional em seu código. 
    return n1 + n2

print(soma(1,2))

x = 0
assert x > 0, 'Deu merda!' #O comando assert é usado para verificar se uma condição é verdadeira e, caso contrário, levanta uma exceção AssertionError. 

