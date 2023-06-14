armas = []

def cadastrar_arma():
    modelo = input("Digite o modelo da arma de fogo: ")
    numero_serie = input("Digite o número de série da arma de fogo: ")
    arma = {"Modelo": modelo, "Número de Série": numero_serie}
    armas.append(arma)
    print("Arma de fogo cadastrada com sucesso!")

def consultar_arma():
    numero_serie = input("Digite o número de série da arma de fogo: ")
    for arma in armas:
        if arma["Número de Série"] == numero_serie:
            print("Modelo:", arma["Modelo"])
            print("Número de Série:", arma["Número de Série"])
            return
    print("Arma de fogo não encontrada.")


cadastrar_arma()
consultar_arma()
