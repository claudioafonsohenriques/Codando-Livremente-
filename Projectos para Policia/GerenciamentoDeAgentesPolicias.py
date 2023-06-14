agentes = []

def cadastrar_agente():
    nome = input("Digite o nome do agente: ")
    matricula = input("Digite a matrícula do agente: ")
    agente = {"Nome": nome, "Matrícula": matricula}
    agentes.append(agente)
    print("Agente cadastrado com sucesso!")

def consultar_agente():
    matricula = input("Digite a matrícula do agente: ")
    for agente in agentes:
        if agente["Matrícula"] == matricula:
            print("Nome:", agente["Nome"])
            print("Matrícula:", agente["Matrícula"])
            return
    print("Agente não encontrado.")


cadastrar_agente()
consultar_agente()
