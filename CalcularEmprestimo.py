def calcular_emprestimo():
    valor_emprestimo = float(input("Digite o valor do empréstimo: "))
    taxa_juros = 0.1  # Exemplo de taxa de juros
    prazo = int(input("Digite o prazo em anos: "))

    taxa_mensal = taxa_juros / 12
    numero_parcelas = prazo * 12

    valor_parcela = (valor_emprestimo * taxa_mensal) / (1 - (1 + taxa_mensal) ** -numero_parcelas)

    print("O valor da parcela mensal é:", valor_parcela)

calcular_emprestimo()
