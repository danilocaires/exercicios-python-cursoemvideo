db_file = "files/db.txt"

def showmenu():
    print("")
    print("="*50)
    print(f"\033[36m{'SISTEMA DE CLIENTES 3.0':^50}\033[m")
    print("="*50)
    print("\n\033[36m1\033[m - Cadastrar novo cliente")
    print("\033[36m2\033[m - Mostrar todos os clientes")
    print("\033[36m3\033[m - Limpar banco de dados")
    print("\033[36m4\033[m - Sair do programa")

def choose():
    while True:
        c = input("\n> ")
        if c == "1" or c== "2" or c == "3" or c == "4":
            return c
        message("Por favor, escolha uma opção válida.", 31)

def displayclients():
    print("-"*50)
    print(f"{'Lista de clientes':^50}\033[m")
    print("-"*50)
    file = open(db_file)
    lista = file.readlines()
    for i in lista:
        nome = '%.15s' % i.split(',')[0]
        idade = i.split(',')[1].replace("\n","")
        print(f"{nome}\t\t\t\t{idade} anos")
    file.close()
    
    print("-"*50)

def addclient():
    print("-"*50)
    print(f"{'Cadastro de novo cliente':^50}\033[m")
    print("-"*50)
    name = input("Nome do cliente: ")
    age = input("Idade do cliente: ")
    file = open(db_file,"a")
    file.write(name+","+age+"\n")
    message("Cliente cadastrado com sucesso!", 32)

def cleardb():
    while True:
        message("Deseja mesmo apagar o banco de dados (s/n)?", 33)
        c = input("\n> ").upper()
        if c == "S":
            file = open(db_file,"w")
            file.close()
            message("Banco de dados apagado com sucesso.", 32)
            break
        elif c== "N":
            message("Operação cancelada.", 31)
            break
        else:
            message("Por favor, escolha uma opção válida.", 31)

        

def message(txt,color):
    print("")
    print("-"*50)
    print(f"\033[{color}m{txt:^50}\033[m")
    print("-"*50)
