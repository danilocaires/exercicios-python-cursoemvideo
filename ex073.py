# crie uma tupla com os 20 primeiros colocados do brasileirao
# mostre: 5 primeiros colocados, os ultimos 4 colocados, uma lista com os times em ordem alfabética, qual a posição do time São Paulo

brasileirao = ("Palmeiras","Internacional","Fluminense","Corinthians","Flamengo","Atlético-PR",
"Atlético-MG","Fortaleza","São Paulo","America-MG","Botafogo","Santos","Goiás","Bragantino","Coritiba","Cuiaba","Ceará SC","Atlético-GO","Avaí","Juventude")

c =0

print("\nAnalisando os times do brasileirão 2022...\n")

print("\nOs 5 primeiros colocados são:")

print(brasileirao[0:5])

print("\nOs times na zona de rebaixamento são:")

print(brasileirao[-4:])

print("\nOs times ordenados em ordem alfabética são: ")
print(sorted(brasileirao))

brasileirao.index("São Paulo")

print("\nA posição que o time do São Paulo está é a {}a".format(brasileirao.index("São Paulo")+1))