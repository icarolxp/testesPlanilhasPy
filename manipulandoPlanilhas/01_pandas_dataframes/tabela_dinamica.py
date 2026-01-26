import pandas as pd
import random

# Listas de opções
vendedores = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo']
regioes = ['Norte', 'Sul', 'Leste', 'Oeste', 'Centro']
produtos = ['Celular', 'Tablet', 'Notebook', 'Monitor']
dados = []

#1. Gerando Vendas Aleatórias
for _ in range(500):
    venda = {
        'Vendedor': random.choice(vendedores),
        'Regiao': random.choice(regioes),
        'Produto': random.choice(produtos),
        'Vendas': random.randint(500, 5000)
    }
    dados.append(venda)

df = pd.DataFrame(dados)

#2. Criando a Tabela Dinâmica
# Index (Linhas): Vendedor
# Columns (Colunas): Região
# Values: Soma das vendas
tabela = df.pivot_table(
    values='Vendas', 
    index='Vendedor', 
    columns='Regiao', 
    aggfunc='sum'
)

# Tratamento de nulos (vendedores que não venderam em certa região)
tabela = tabela.fillna(0)

# Adicionando coluna de total
tabela['Total_Geral'] = tabela.sum(axis=1)

print("Matriz de Vendas por Região")
print(tabela.round(2))