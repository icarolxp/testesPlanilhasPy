import pandas as pd
import random
from datetime import datetime, timedelta

usuarios = ['User_Admin', 'User_Vendas', 'User_Visitante', 'User_Dev']
dados = []

# Data inicial
inicio = datetime(2023, 1, 1)

for _ in range(200):
    # Sorteia dias a adicionar (0 a 365)
    dias_extra = random.randint(0, 365)
    data_log = inicio + timedelta(days=dias_extra)
    
    # Converte para string para simular leitura de CSV
    dados.append({
        'Data_String': data_log.strftime('%Y-%m-%d'),
        'Usuario': random.choice(usuarios)
    })

df = pd.DataFrame(dados)

# 1. Converter para um formato real
df['Data'] = pd.to_datetime(df['Data_String'])

# 2. Extrair informações
df['Mes'] = df['Data'].dt.month_name()
df['Dia_Semana'] = df['Data'].dt.day_name()

# 3. Análise: Qual dia da semana tem mais acessos?
acessos_por_dia = df['Dia_Semana'].value_counts()

print("Amostra de Acessos")
print(df.head())

print("\nRanking de Acessos por Dia da Semana ")
print(acessos_por_dia)