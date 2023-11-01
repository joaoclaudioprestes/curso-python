number = int(input("Digite um valor para calcular a tabuada: "))

cont = 1 

while cont <=10:
    res = cont * number
    print("{} x {} = {}".format(cont, number, res))
    cont += 1