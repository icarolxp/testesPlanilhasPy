import pandas as pd

# 1. Dados de vendas
dados = {
    'Vendedor': ['Ana', 'Carlos', 'Ana', 'Beatriz', 'Carlos', 'Beatriz'],
    'Regiao': ['Sul', 'Norte', 'Sul', 'Sudeste', 'Norte', 'Sudeste'],
    'Venda': [1200, 3400, 500, 1500, 2100, 4000]
}

df = pd.DataFrame(dados)

print("--- DataFrame Original ---")
print(df)
print("\n" + "="*30 + "\n")

# 2. Agrupando por Vendedor para ver o total vendido
# Equivalente a 'SOMASE' no Excel
vendas_por_vendedor = df.groupby('Vendedor')['Venda'].sum().reset_index()

# 3. Agrupando por Região para ver a média de vendas
media_por_regiao = df.groupby('Regiao')['Venda'].mean().reset_index()

print("--- Total de Vendas por Vendedor ---")
print(vendas_por_vendedor)

print("\n--- Média de Vendas por Região ---")
print(media_por_regiao)

# 4. Salvando os resultados em arquivos Excel (opcional)

vendas_por_vendedor.to_excel("relatorio_agrupado.xlsx", index=False)