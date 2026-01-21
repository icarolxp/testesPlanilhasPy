import xlsxwriter

workbook = xlsxwriter.Workbook('vendas_grafico.xlsx')
worksheet = workbook.add_worksheet()

# Dados em colunas
titulos = ['Mês', 'Vendas']
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai']
vendas = [1000, 1200, 900, 1500, 1800]

# Escrever os dados
worksheet.write_row('A1', titulos)
worksheet.write_column('A2', meses)
worksheet.write_column('B2', vendas)

#CRIANDO O GRÁFICO

# 1. Criar o objeto gráfico (tipo coluna/barra)
chart = workbook.add_chart({'type': 'column'})

# 2. Configurar a série de dados (onde estão os valores?)
chart.add_series({
    'name':       '=Sheet1!$B$1',  # Título da série ("Vendas")
    'categories': '=Sheet1!$A$2:$A$6', # Eixo X (Meses)
    'values':     '=Sheet1!$B$2:$B$6', # Eixo Y (Valores)
    'data_labels': {'value': True},    # Mostrar números em cima das barras
})

# 3. Adicionar títulos e estilo
chart.set_title ({'name': 'Performance de Vendas 2024'})
chart.set_x_axis({'name': 'Meses'})
chart.set_y_axis({'name': 'Valor (R$)'})

# Estilo visual (existem dezenas de estilos numerados)
chart.set_style(11)

# 4. Inserir o gráfico na planilha
worksheet.insert_chart('D2', chart)

workbook.close()
print("Planilha 'vendas_grafico.xlsx' criada com gráfico!")