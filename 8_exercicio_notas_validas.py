while True:
    nota_aluno = int(input('Digite a nota do aluno: '))
    if nota_aluno >= 0 and nota_aluno <=10:
        print(f'Nota armazenadacom sucesso {nota_aluno}')
        break
    else:
        print('Nota inválida digite novamente')
        continue