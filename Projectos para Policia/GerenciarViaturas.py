viaturas = []

def cadastrar_viatura():
    modelo = input("Digite o modelo da viatura: ")
    placa = input("Digite a placa da viatura: ")
    viatura = {"Modelo": modelo, "Placa": placa}
    viaturas.append(viatura)
    print("Viatura cadastrada com sucesso!")

def consultar_viatura():
    placa = input("Digite a placa da viatura: ")
    for viatura in viaturas:
        if viatura["Placa"] == placa:
            print("Modelo:", viatura["Modelo"])
            print("Placa:", viatura["Placa"])
            return
    print("Viatura não encontrada.")

cadastrar_viatura()
consultar_viatura()
