import pandas as pd

# 1. Criar uma base de dados de funcionários
dados_rh = {
    'Nome': ['João', 'Maria', 'Carlos', 'Ana', 'Pedro', 'Beatriz'],
    'Departamento': ['TI', 'Vendas', 'TI', 'RH', 'Vendas', 'TI'],
    'Salario': [5000, 3200, 7500, 4000, 3000, 6200],
    'Anos_Empresa': [2, 5, 8, 3, 1, 4]
}

df = pd.DataFrame(dados_rh)

print("--- Tabela Original ---")
print(df)
print("\n")

# 2. Objetivo: Filtrar apenas funcionários de 'TI' que ganham mais de 6000
# Sintaxe do Pandas: df[ (condicao1) & (condicao2) ]

filtro = (df['Departamento'] == 'TI') & (df['Salario'] > 6000)
df_ti_senior = df[filtro]

print("--- Resultado do Filtro (TI & Salário > 6000) ---")
print(df_ti_senior)

# 3. Salvar o resultado filtrado
nome_arquivo = 'funcionarios_ti_senior.xlsx'
df_ti_senior.to_excel(nome_arquivo, index=False, engine='openpyxl')

print(f"\nRelatório filtrado salvo em: {nome_arquivo}")