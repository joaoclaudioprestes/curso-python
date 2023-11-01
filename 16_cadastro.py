# Cadastrar pessoas
pessoas = []
while True:
    decisao = input('Deseja cadastrar uma pessoa?\n1. Sim\n2. Não\n... ')

    if decisao == 2:
        break

    print('--- CADASTRO ---')
    
    pessoa = ({'nome': input('Digite o nome: '),
                'idade': int(input('Digite a sua idade: ')),
                'altura': float(input('Digite a altura: ')),
                'peso': float(input('Digite o peso: '))})
    
    pessoas.append(pessoa)

    print(pessoas)
