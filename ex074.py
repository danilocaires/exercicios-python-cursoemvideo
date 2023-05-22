# crie 5 numeros aleatórios e colocar em uma tupla
# mostre os numeros gerados e tambem indique o menor e o maior valor da tupla

from random import randint

tupla = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))

print(f"\nNúmeros gerados: {tupla}")
print(f"Maior número: {max(tupla)}")
print(f"Menor número: {min(tupla)}\n")