# Definimos como uma pesso é
class Pessoas: 
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistema(self):
        print(f'{self.nome} - Logou no sistema')

p1 = Pessoas('João Prestes', 18, '57480517882')
p2 = Pessoas('Carlos', 16, '5747865882')

print(p1.nome, p1.idade, p1.cpf)
p1.logar_sistema()
print(p2.nome, p2.idade, p2.cpf)
p2.logar_sistema()

# F070