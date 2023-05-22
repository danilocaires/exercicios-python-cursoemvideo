# Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples
# O sistema só vai ter duas opções: Cadastrar uma nova pessoa e listar as pessoas cadastradas
from time import sleep
import sistema as s

while True:
    s.showmenu()
    option = s.choose()
    if option == "1":
        s.addclient()
    elif option == "2":
        s.displayclients()
    elif option == "3":
        s.cleardb()
    elif option == "4":
        s.message("Encerrando o programa. Volte sempre! :)",32)
        break
    else:
        s.message("Por favor, escolha uma opção válida.", 31)
    sleep(1.5)
