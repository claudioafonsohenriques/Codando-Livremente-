recursos = []

def cadastrar_recurso():
    tipo = input("Digite o tipo do recurso: ")
    quantidade = input("Digite a quantidade do recurso: ")
    recurso = {"Tipo": tipo, "Quantidade": quantidade}
    recursos.append(recurso)
    print("Recurso cadastrado com sucesso!")

def consultar_recurso():
    tipo = input("Digite o tipo do recurso: ")
    for recurso in recursos:
        if recurso["Tipo"] == tipo:
            print("Tipo:", recurso["Tipo"])

cadastrar_recurso()
consultar_recurso()