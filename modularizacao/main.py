import minha_lib #Traz tudo....
from minha_lib import y #importa somente uma coisa
from my_functions.functions import ok_soma as soma # "as"" nomeia como utilizaremos neste arquivo
import math 

print(minha_lib.x)
print(y)
print(soma(2))

print(math.cos(75))

minha_lib.ok_sub()