# Variavel
from datetime import datetime
import time
Coldown = 0
Profile = ""
Senha = ""
Old_Profile = "Null"
Old_Senha = "NullADM"
Primeiro_Cadastro = False
Login = False
Codigos = ["infor", "print", "calcular"]
Terminal = "Null"

# Cadastro
print("BEM VINDO AO MENU PYTHON!")
print("Você ja tem um conta?")
Primeiro_Cadastro = input("(Sim/Não): ")

# Primeiro_Cadastro = SIM
if Primeiro_Cadastro == "Sim" or Primeiro_Cadastro == "sim":
    Profile = input("Digite seu profile: ")
    Senha = input("Digite sua Senha: ")
    if Profile == Old_Profile and Senha == Old_Senha:
        print("sorry ADM! ainda não tem nada! hehe...")
    else:
        print(f"seu profile({Profile}) ou sua senha({Senha}) esta errada.")
        time.sleep(1)
        print("Tente novante mais tarde...")
        # ---> não prosegue mais
# Primeiro_Cadastro = NÃO
else:
    print("Vamos começar criando seu login")
    time.sleep(1)
    Profile = input("Digite seu nome: ")
    Senha = input("Digite sua senha: ")
    while Coldown < 4:
        print("Verificando...", end="\r")
        time.sleep(0.5)
        print("Verificando.. ", end="\r")
        time.sleep(0.5)
        print("Verificando. ", end="\r")
        time.sleep(0.5)
        Coldown = Coldown + 1
    print("Conta criada com sucesso!")
    time.sleep(1.5)
    print("Abrindo painel.")
    time.sleep(1)
    Login = True

# Painel
if Login == True:
    print(r""" ____ ___  _ _____ _     ____  _     
/  __\\  \///__ __| \ /|/  _ \/ \  /|
|  \/| \  /   / \ | |_||| / \|| |\ ||
|  __/ / /    | | | | ||| \_/|| | \||
\_/   /_/     \_/ \_/ \|\____/\_/  \|
                                     """)
    print(Codigos, "    V1.0 Beta")  # "infor", "print", "calcular"
    Terminal = input("Enter Code: ")

# Codigo
    if Terminal == "infor" or Terminal == "Infor":
        print("Codigo Infor ativado!")
        print(f"Profile: {Profile}")
        time.sleep(0.5)
        print(f"Senha: {Senha}")
        time.sleep(0.5)
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        time.sleep(0.5)
        print(f"Dados do Usuario {Profile}")
    elif Terminal == "print" or Terminal == "Print":
        print("Codigo Print ativado!")
        CPrint = input("Digite o que deseja printar: ")
        time.sleep(0.5)
        print(CPrint)
    elif Terminal == "calcular" or Terminal == "Calcular":
        print("Codigo Calcular ativado!")
        Operação = input("Digite a expreção: ")
        # operação basica
    if "+" in Operação:  # soma basica
        print("Soma detectada!")
        print("Resultado: ", eval(Operação))

    elif "-" in Operação:  # subtração basica
        print("Subtração detectada!")
        print("Resultado: ", eval(Operação))

    elif "*" in Operação:  # multiplicação basica
        print("Multiplicação detectada!")
        print("Resultado: ", eval(Operação))

    elif "/" in Operação:  # disão basica
        print("Divisão Detectada!")
        print("Resultado: ", eval(Operação))

    elif Operação == "Tabuada" or Operação == "tabuada":  # tabuada de 1 a 10
        print("Tabuada detectada!")
        Numero = int(input("Digite o numero: "))
        for TAB in range(1, 11):
            print(f"{Numero} x {TAB} = {Numero * TAB}")
