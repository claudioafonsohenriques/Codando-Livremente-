ocorrencias = []

def registrar_ocorrencia():
    numero_ocorrencia = input("Digite o número da ocorrência: ")
    descricao = input("Digite a descrição da ocorrência: ")
    ocorrencia = {"Número": numero_ocorrencia, "Descrição": descricao}
    ocorrencias.append(ocorrencia)
    print("Ocorrência registrada com sucesso!")

def consultar_ocorrencia():
    numero_ocorrencia = input("Digite o número da ocorrência: ")
    for ocorrencia in ocorrencias:
        if ocorrencia["Número"] == numero_ocorrencia:
            print("Número:", ocorrencia["Número"])
            print("Descrição:", ocorrencia["Descrição"])
            return
    print("Ocorrência não encontrada.")

registrar_ocorrencia()
consultar_ocorrencia()
