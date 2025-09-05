print("=== Valor Presente de Parcela Futura ===\n")

valor_futuro = float(input("    Insira o Valor Futuro: R$"))
taxa_juros = float(input("    Insira a taxa de juros mensal: "))
tempo = float(input("    Insira o tempo em meses: "))

valor_presente = valor_futuro / (1 + taxa_juros)**tempo

print(f'\n    Valor presente: {valor_presente:.2f}')