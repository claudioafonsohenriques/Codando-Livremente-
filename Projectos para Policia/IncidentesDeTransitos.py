incidentes_transito = []

def registrar_incidente_transito():
    local = input("Digite o local do incidente de trânsito: ")
    data = input("Digite a data do incidente de trânsito: ")
    incidente = {"Local": local, "Data": data}
    incidentes_transito.append(incidente)
    print("Incidente de trânsito registrado com sucesso!")

def consultar_incidente_transito():
    local = input("Digite o local do incidente de trânsito: ")
    for incidente in incidentes_transito:
        if incidente["Local"] == local:
            print("Local:", incidente["Local"])
            print("Data:", incidente["Data"])
            return
    print("Incidente de trânsito não encontrado.")


registrar_incidente_transito()
consultar_incidente_transito()
