def calcular_consumo_energia():
    leitura_atual = float(input("Digite a leitura atual: "))
    leitura_anterior = float(input("Digite a leitura anterior: "))
    preco_kwh = 0.5  # Exemplo de preço do kWh

    consumo_mensal = leitura_atual - leitura_anterior
    valor_fatura = consumo_mensal * preco_kwh

    print("O consumo mensal é:", consumo_mensal, "kWh")
    print("O valor da fatura é:", valor_fatura)

calcular_consumo_energia()
