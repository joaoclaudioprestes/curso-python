from pympler.asizeof import asizeof

my_list = [1, 2, 3, 4, 5]
size = asizeof.asizeof(my_list)
print(f'O tamanho da lista é {size} bytes')
