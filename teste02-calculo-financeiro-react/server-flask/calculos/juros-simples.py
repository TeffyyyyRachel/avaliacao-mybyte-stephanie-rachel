print("======= Juros Simples =======\n")

capital_inicial = float(input("Insira o Capital Inicial: R$"))
taxa_mes = float(input("Insira a taxa mensal: "))
tempo_meses = int(input("Insira o tempo em meses: "))

juros = capital_inicial * taxa_mes * tempo_meses
montante = capital_inicial + juros

print(f'\nMontante: {montante:.2f}')
print(f'Juros: {juros:.2f}')