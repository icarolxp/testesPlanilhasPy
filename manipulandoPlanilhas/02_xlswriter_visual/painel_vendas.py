import pandas as pd
import random

# 1. Preparando os dados (simulando um ano de vendas)
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
dados = []

for mes in meses:
    receita = random.randint(20000, 50000)
    despesa = random.randint(15000, 35000)
    lucro = receita - despesa
    dados.append([mes, receita, despesa, lucro])

df = pd.DataFrame(dados, columns=['Mês', 'Receita', 'Despesa', 'Lucro'])

# 2. Iniciando o Writer com a engine XlsxWriter
arquivo_saida = 'relatorio_visual.xlsx'
writer = pd.ExcelWriter(arquivo_saida, engine='xlsxwriter')

# Converte o DataFrame para Excel (mas não salva ainda)
df.to_excel(writer, sheet_name='Dashboard', index=False)

# 3. Acessando o objeto de trabalho (workbook e worksheet) para customizar
workbook = writer.book
worksheet = writer.sheets['Dashboard']

# 4. Criando um gráfico de colunas para Receita e Despesa
chart = workbook.add_chart({'type': 'column'})

# Configurando as séries do gráfico (Receita vs Despesa)
# Sintaxe: [sheetname, first_row, first_col, last_row, last_col]
qtd_linhas = len(df) + 1 
chart.add_series({
    'name':       '=Dashboard!$B$1',
    'categories': ['Dashboard', 1, 0, qtd_linhas-1, 0], # Coluna Mês
    'values':     ['Dashboard', 1, 1, qtd_linhas-1, 1], # Coluna Receita
})
chart.add_series({
    'name':       '=Dashboard!$C$1',
    'categories': ['Dashboard', 1, 0, qtd_linhas-1, 0],
    'values':     ['Dashboard', 1, 2, qtd_linhas-1, 2], # Coluna Despesa
})

chart.set_title({'name': 'Balanço Anual'})
worksheet.insert_chart('F2', chart) # Insere o gráfico na célula F2

# condicional de formatação para a coluna de Lucro
# Formato verde para lucro positivo
formato_verde = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'})
# Formato vermelho para prejuízo (se houver)
formato_vermelho = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})

# Aplica na coluna D (Lucro), da linha 2 até a final
worksheet.conditional_format(f'D2:D{qtd_linhas}', {
    'type': 'cell',
    'criteria': '>',
    'value': 0,
    'format': formato_verde
})
worksheet.conditional_format(f'D2:D{qtd_linhas}', {
    'type': 'cell',
    'criteria': '<',
    'value': 0,
    'format': formato_vermelho
})

# Salvando
writer.close()
print(f"Arquivo '{arquivo_saida}' gerado com gráficos e cores!")