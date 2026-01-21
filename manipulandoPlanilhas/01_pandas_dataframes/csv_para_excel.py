import pandas as pd
import os

# Nome dos arquivos
arquivo_csv = 'vendas_brutas.csv'
arquivo_excel = 'relatorio_vendas.xlsx'

# 1. Vamos criar dados fictícios e salvar como CSV (para simular uma base de dados)
dados = {
    'Produto': ['Teclado', 'Rato', 'Monitor', 'Cabo HDMI', 'Headset'],
    'Preco': [150.50, 80.90, 1200.00, 35.00, 250.00],
    'Quantidade': [10, 25, 5, 50, 12],
    'Loja': ['Amazonas', 'São Paulo', 'Amazonas', 'Rio de Janeiro', 'São Paulo']
}

# Criar o DataFrame
df = pd.DataFrame(dados)

# Salvar como CSV (sem índice)
df.to_csv(arquivo_csv, index=False)
print(f"Planilha CSV '{arquivo_csv}' criado com sucesso.")

print("------------------------------------------------")

# 2. Agora começa a automação real: Ler o CSV e converter para Excel
print(f"Lendo '{arquivo_csv}' e convertendo para Excel...")

try:
    # Ler o CSV
    df_leitura = pd.read_csv(arquivo_csv)
    
    # Adicionar uma coluna nova (Faturação Total) antes de salvar
    df_leitura['Total_Vendas'] = df_leitura['Preco'] * df_leitura['Quantidade']
    
    # Salvar como Excel
    df_leitura.to_excel(arquivo_excel, index=False, engine='openpyxl')
    
    print(f"Sucesso! A planilha '{arquivo_excel}' foi criada.")
    print("Abra a pasta para conferir o resultado.")
    
except Exception as e:
    print(f"Ocorreu um erro: {e}")