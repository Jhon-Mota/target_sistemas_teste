from datetime import datetime

valor = float(input("Digite o valor da dívida: R$ "))
data_vencimento = input("Digite a data de vencimento (dd/mm/aaaa): ")

data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")

data_hoje = datetime.now()

dias_atraso = (data_hoje - data_vencimento).days

juros = valor * 0.025 * dias_atraso

valor_total = valor + juros

print(f"\nDias de atraso: {dias_atraso}")
print(f"Juros: R$ {juros:.2f}")
print(f"Valor total: R$ {valor_total:.2f}")
