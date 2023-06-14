def rastrear_encomenda():
    codigo_rastreamento = input("Digite o código de rastreamento: ")
    status = obter_status_encomenda(codigo_rastreamento)

    print("O status da encomenda é:", status)

rastrear_encomenda()
