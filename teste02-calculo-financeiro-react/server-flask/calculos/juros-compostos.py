print("====== Juros Compostos ======\n")

capital_inicial = float(input("Insira o Capital Inicial: R$"))
taxa_mes = float(input("Insira a taxa mensal: "))
tempo_meses = int(input("Insira o tempo em meses: "))

montante = capital_inicial * (1 + taxa_mes)**tempo_meses
juros = montante - capital_inicial

print(f'\nMontante: {montante:.2f}')
print(f'Juros compostos: {juros:.2f}')