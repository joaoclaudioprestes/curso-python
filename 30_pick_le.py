# Cerialização de objetos - pegar algo que está em memoria e torna-lo percistente
import pickle

class Pessoa:
    nome = 'joao'
    idade = 18

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoas('Teste', 25)

with open('arquivo.pkl', 'wb') as arq:
    pickle.dump(arq, p1)

