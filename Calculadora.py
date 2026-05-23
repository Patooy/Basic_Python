Loop = True

while Loop == True:
    print("                                               ")
    print("--------------------------")
    print("Calculadora basica!")
    print("Lista: Tabuada, Porcentagem, multiplicação(*), divisão(/), adição(+), subtração(-)")
    print("---------------------------")
    Operacao = input("Digite a expreção: ")

    # operações multi mista
    if "+" in Operacao and "-" in Operacao and "*" in Operacao and "/" in Operacao:
        print("Multi fatores detectado!soma, subtração, multiplicação e divisão")
        print("Resultado: ", eval(Operacao))

    # operações mistas 2
    elif "+" in Operacao and "-" in Operacao:
        print("Operacao mista detectada! soma e subtração")
        print("Resultado: ", eval(Operacao))

    elif "+" in Operacao and "*" in Operacao:
        print("Operacao mista detectada! soma e multiplicação")
        print("Resultado: ", eval(Operacao))

    elif "+" in Operacao and "/" in Operacao:
        print("Operacao mista detectada! soma e divisão")
        print("Resultado: ", eval(Operacao))

    elif "-" in Operacao and "*" in Operacao:
        print("Operacao mista detectada! subtração e multiplicação")
        print("Resultado: ", eval(Operacao))

    elif "-" in Operacao and "/" in Operacao:
        print("Operacao mista detectada! subtração e divisão")
        print("Resultado: ", eval(Operacao))

    elif "*" in Operacao and "/" in Operacao:
        print("Operacao mista detectada! multiplicação e divisão")
        print("Resultado: ", eval(Operacao))

    # Operacao basica
    elif "+" in Operacao:  # soma basica
        print("Soma detectada!")
        print("Resultado: ", eval(Operacao))

    elif "-" in Operacao:  # subtração basica
        print("Subtração detectada!")
        print("Resultado: ", eval(Operacao))

    elif "*" in Operacao:  # multiplicação basica
        print("Multiplicação detectada!")
        print("Resultado: ", eval(Operacao))

    elif "/" in Operacao:  # disão basica
        print("Divisão Detectada!")
        print("Resultado: ", eval(Operacao))

    elif Operacao == "Tabuada" or Operacao == "tabuada":  # tabuada de 1 a 10
        print("Tabuada detectada!")
        Numero = int(input("Digite o numero: "))
        for TAB in range(1, 11):
            print(f"{Numero} x {TAB} = {Numero * TAB}")

    elif Operacao == "Porcentagem" or Operacao == "porcentagem":
        total = float(input("Digite o numero total: "))
        porcento = float(input("Digite a %: "))
        print("Resposta: ", end="")
        print((total * porcento) / 100)
    else:
         print("Erro: expresão não corespondida!")
         break
         