import pandas as pd

# 1. lendo o arquivo de vendas gerado anteriormente
# O pandas procura o arquivo na mesma pasta onde o script está rodando
try:
    df = pd.read_csv('vendas_loja.csv')
    print("Arquivo carregado com sucesso!\n")
except FileNotFoundError:
    print("Erro: O arquivo 'vendas_loja.csv' não existe. Rode o gerador primeiro.")
    exit()

# 2. Criando uma coluna nova (Faturamento = Quantidade * Preço)
df['faturamento_total'] = df['quantidade'] * df['preco_unitario']

# 3. Análises

# Total vendido pela loja
total_geral = df['faturamento_total'].sum()

# Qual produto vendeu mais (em dinheiro)?
ranking_produtos = df.groupby('produto')['faturamento_total'].sum().sort_values(ascending=False)

# Quantas vendas ocorreram por cidade?
vendas_por_cidade = df['cidade'].value_counts()

print(f"--- Faturamento Total da Loja: R$ {total_geral:,.2f} ---")
print("\n--- Ranking de Faturamento por Produto ---")
print(ranking_produtos)
print("\n--- Número de Vendas por Cidade ---")
print(vendas_por_cidade)