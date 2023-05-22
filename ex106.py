# faça um mini-sistema que utilize o interactive help do Python
# O user digita o comando e o manual vai aparecer
# Quando o user digitar FIM o programa se encerra

def ajuda(texto):
    print(f"Acessando o manual do comando '{texto}'")
    help(texto)

comando = ""
while True:
    comando = str(input("Função ou biblioteca: "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)