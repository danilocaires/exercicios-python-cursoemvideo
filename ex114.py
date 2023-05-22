# Crie um código em Python que verifica se o site Pudim está acessível pelo seu computador

from urllib import request

try:
    site = request.urlopen("http://www.pudim.com.br").getcode() == 200
except:
    print("\033[31mWhere is pudim? Is he safe? Is he alright?")
else:
    print("\033[32mO pudim tá ON! :)")
    