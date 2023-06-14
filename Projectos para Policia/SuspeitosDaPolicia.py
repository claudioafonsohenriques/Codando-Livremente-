suspeitos = []

def cadastrar_suspeito():
    nome = input("Digite o nome do suspeito: ")
    idade = input("Digite a idade do suspeito: ")
    suspeito = {"Nome": nome, "Idade": idade}
    suspeitos.append(suspeito)
    print("Suspeito cadastrado com sucesso!")

def consultar_suspeito():
    nome = input("Digite o nome do suspeito: ")
    for suspeito in suspeitos:
        if suspeito["Nome"] == nome:
            print("Nome:", suspeito["Nome"])
            print("Idade:", suspeito["Idade"])
            return
    print("Suspeito não encontrado.")


cadastrar_suspeito()
consultar_suspeito()
