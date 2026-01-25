import pandas as pd

# Criando uma tabela de produtos antiga
dados = {
    'Código': [101, 102, 103, 104],
    'Produto': ['Teclado Mecânico', 'Mouse Gamer', 'Monitor 24"', 'Headset'],
    'Preço_Atual': [250.00, 120.00, 800.00, 300.00],
    'Estoque': [15, 30, 8, 12]
}

df = pd.DataFrame(dados)
df.to_excel('lista_produtos.xlsx', index=False)
print("Arquivo original 'lista_produtos.xlsx' criado.")