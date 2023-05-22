print("\n")

# today
from datetime import date
print(date.today())
print(date.today().day)
print(date.today().month)
print(date.today().year)

print("\n\n")

print("Duas casas decimais: {:.2f} ")
print(f"Escrever em 20 espaços: {'Teste':20} ")
print(f"Alinhar para direita: {'Teste':>20} ")
print(f"Alinhar para esquerda: {'Teste':<20} ")
print(f"Centralizar: {'Teste':^20} ")

print("\n\n")

#font format
print("\033[0mHello World!\033[m") # none
print("\033[1mHello World!\033[m") # bold
print("\033[4mHello World!\033[m\n") # underscore
print("\033[7mHello World!\033[m") # negative

print("\n")

# font color
print("\033[30mHello World!\033[m") #gray
print("\033[31mHello World!\033[m") #red
print("\033[32mHello World!\033[m") #green
print("\033[33mHello World!\033[m") #yellow
print("\033[34mHello World!\033[m") #blue
print("\033[35mHello World!\033[m") #purple
print("\033[36mHello World!\033[m") #cyan
print("\033[37mHello World!\033[m") #white

print("\n")

# bg color
print("\033[40mHello World!\033[m") #black
print("\033[41mHello World!\033[m") #red
print("\033[42mHello World!\033[m") #green
print("\033[43mHello World!\033[m") #yellow
print("\033[44mHello World!\033[m") #blue
print("\033[45mHello World!\033[m") #purple
print("\033[46mHello World!\033[m") #cyan
print("\033[47mHello World!\033[m") #white

print("\n\n")

# LISTAS

sobremesas = ["Pudim","Sorvete","Bis","Torta","Bolo"]

# adiciona no final da lista
sobremesas.append("Gelatina")

# adiciona em uma posição específica
sobremesas.insert(2,"Gelatina")

# remover uma entrada da lista
del sobremesas[3]
sobremesas.pop(3)

# remover a ultima entrada da lista
sobremesas.pop()

# verificar se o valor está na lista

if "Sorvete" in sobremesas:
    print("Está na lista!")

# ordem alfabética
sobremesas.sort()

# ordem reversa
sobremesas.sort(reverse=True)

# elimina um valor especifico
sobremesas.remove("Sorvete")

# copiar uma lista

sobremesas2 = sobremesas[:]

# inicializar uma lista

valores = list()
valores = []

# inicializar uma lista com range

valores = list(range(4,11))

# tamanho da lista

len(valores)

# puxar valores e indices de uma lista

for c,v in enumerate(valores):
    print(f"Posição {c}, valor {v}")

# duplicar uma lista
lista = []
copialista = lista[:]

####### LISTAS COMPOSTAS #########

cadastro = []
pessoa = ["Danilo", 31]

cadastro.append(pessoa[:])


# DICIONÁRIOS

dados = {}

dados['nome'] = "Danilo"
dados['idade'] = 31
dados['sexo'] = "M"

dados.values() # Danilo, 31 e M
dados.keys() # nome, idade e sexo
dados.items() # nome: Danilo, idade:31, sexo:M

dados.copy()