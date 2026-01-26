import pandas as pd
import random

dados = []

#1. Gerando Folha de Pagamento
for i in range(100):
    dados.append({
        'Funcionario': f'Func_{i+1:03d}',
        'Salario': random.randint(1500, 15000)
    })

df = pd.DataFrame(dados)

#2. Definindo Regra de Negócio para Cálculo do IR
def calcular_imposto_ir(salario):
    if salario <= 2259:
        return 0.0
    elif salario <= 2826:
        return salario * 0.075
    elif salario <= 3751:
        return salario * 0.150
    elif salario <= 4664:
        return salario * 0.225
    else:
        return salario * 0.275

# O método .apply() executa a função para cada linha da coluna
df['Imposto'] = df['Salario'].apply(calcular_imposto_ir)
df['Liquido'] = df['Salario'] - df['Imposto']

# Ordenando para ver os maiores salários primeiro
df_ordenado = df.sort_values('Salario', ascending=False)

print("Top 5 Salários e Impostos Retidos")
print(df_ordenado.head())

print(f"\nTotal Retido na Fonte: R$ {df['Imposto'].sum():,.2f}")