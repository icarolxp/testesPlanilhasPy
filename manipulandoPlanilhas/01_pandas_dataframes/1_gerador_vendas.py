import pandas as pd
import random

# Criando dados para salvar no arquivo
produtos_lista = ['Notebook', 'Smartphone', 'Fone Bluetooth', 'Monitor', 'Teclado']
cidades_lista = ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Belo Horizonte']

dados = []

# Gerando 50 vendas aleatórias
for i in range(50):
    item = {
        'id_venda': 1000 + i,
        'produto': random.choice(produtos_lista),
        'cidade': random.choice(cidades_lista),
        'quantidade': random.randint(1, 5),
        'preco_unitario': random.choice([1500, 2500, 200, 800, 150])
    }
    dados.append(item)

df = pd.DataFrame(dados)

nome_arquivo = 'vendas_loja.csv'
df.to_csv(nome_arquivo, index=False)

print(f"Sucesso! O arquivo '{nome_arquivo}' foi criado com {len(df)} linhas.")