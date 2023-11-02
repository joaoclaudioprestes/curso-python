# arquivo = open('usuario.txt', 'r') 
# # i = 0
# # while True:
# #     if i > 1:
# #         break
# #     arquivo.write(input('Digite o nome do usuario: ') + '\n' + input('Digite a idade do usuario: ') + '\n')
# #     i += 1

# resultados = arquivo.read()

# print(resultados)


# arquivo.close()

with open('pessoas.txt', 'r') as arq: 
    # with basicamente executa o que tem que executar e realiza o fechamento do arquivo
    x = arq.read()
    print(x)