lista_par = []

for i in range(1,1000):
    par = i%2

    if par == 0:
        lista_par.append(i)

exibir = input("Deseja exibir os números pares? [S | N]\n...")

if exibir == 'S' or 's':
    print(lista_par)
else:
    print('OK')
