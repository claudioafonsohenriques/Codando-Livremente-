treinamentos = []

def cadastrar_treinamento():
    nome = input("Digite o nome do treinamento ou capacitação: ")
    data = input("Digite a data do treinamento ou capacitação: ")
    treinamento = {"Nome": nome, "Data": data}
    treinamentos.append(treinamento)
    print("Treinamento ou capacitação cadastrado com sucesso!")

def consultar_treinamento():
    nome = input("Digite o nome do treinamento ou capacitação: ")
    for treinamento in treinamentos:
        if treinamento["Nome"] == nome:
            print("Nome:", treinamento["Nome"])
            print("Data:", treinamento["Data"])
            return
    print("Treinamento ou capacitação não encontrado.")

cadastrar_treinamento()
consultar_treinamento()
