def calcular_salario_liquido():
    salario_bruto = float(input("Digite o salário bruto: "))
    taxa_impostos = 0.2  # Exemplo de taxa de impostos
    taxa_contribuicoes = 0.1  # Exemplo de taxa de contribuições
    taxa_outros_encargos = 0.05  # Exemplo de taxa de outros encargos

    calcular_impostos = salario_bruto * taxa_impostos
    calcular_contribuicoes = salario_bruto * taxa_contribuicoes
    calcular_outros_encargos = salario_bruto * taxa_outros_encargos

    salario_liquido = salario_bruto - calcular_impostos - calcular_contribuicoes - calcular_outros_encargos

    print("O salário líquido é:", salario_liquido)

calcular_salario_liquido()
