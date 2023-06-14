patrulhas = []

def cadastrar_patrulha():
    nome = input("Digite o nome da patrulha: ")
    localizacao = input("Digite a localização da patrulha: ")
    patrulha = {"Nome": nome, "Localização": localizacao}
    patrulhas.append(patrulha)
    print("Patrulha cadastrada com sucesso!")

def consultar_patrulha():
    nome = input("Digite o nome da patrulha: ")
    for patrulha in patrulhas:
        if patrulha["Nome"] == nome:
            print("Nome:", patrulha["Nome"])
            print("Localização:", patrulha["Localização"])
            return
    print("Patrulha não encontrada.")


cadastrar_patrulha()
consultar_patrulha()
