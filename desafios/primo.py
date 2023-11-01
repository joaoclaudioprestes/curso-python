number = int(input("Digite um número: "))
resNumber1 = number%1
resNumber2 = number%number

print(resNumber1)
print(resNumber2)

if (resNumber1 == 0) and (resNumber2 == 0):
    print('é primo')
else:
    print("não e primo")