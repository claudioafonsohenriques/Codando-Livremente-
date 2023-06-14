def converter_moeda():
    valor_moeda_estrangeira = float(input("Digite o valor em moeda estrangeira: "))
    taxa_cambio = 0.5  # Exemplo de taxa de câmbio

    valor_moeda_local = valor_moeda_estrangeira * taxa_cambio

    print("O valor em moeda local é:", valor_moeda_local)

converter_moeda()
