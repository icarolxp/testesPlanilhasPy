import xlsxwriter

# Criar o arquivo e a aba
workbook = xlsxwriter.Workbook('notas_alunos.xlsx')
worksheet = workbook.add_worksheet('Resultados')

# Dados para escrever
dados = [
    ['Aluno', 'Nota'],
    ['Ana', 85],
    ['Bruno', 40],
    ['Carlos', 92],
    ['Daniela', 55],
    ['Eduardo', 30],
]

# Escrever os dados na planilha (linha por linha)
row = 0
col = 0

for nome, nota in dados:
    worksheet.write(row, col, nome)
    worksheet.write(row, col + 1, nota)
    row += 1
# Definir os formatos (estilos)
formato_aprovado = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'}) # Verde
formato_reprovado = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'}) # Vermelho

# Aplicar formatação condicional na coluna B (Notas)
# Linhas 1 a 5 (B2:B6)
worksheet.conditional_format('B2:B6', {
    'type': 'cell',
    'criteria': '>=',
    'value': 60,
    'format': formato_aprovado
})

worksheet.conditional_format('B2:B6', {
    'type': 'cell',
    'criteria': '<',
    'value': 60,
    'format': formato_reprovado
})

workbook.close()
print("Planilha 'notas_alunos.xlsx' criada com cores automáticas!")