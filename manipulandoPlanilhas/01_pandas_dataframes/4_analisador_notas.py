import pandas as pd

# Carregando o CSV gerado
df = pd.read_csv('notas_escolares.csv')

print("--- Notas Originais ---")
print(df)
print("\n" + "="*30 + "\n")

# Vamos calcular a média das 3 matérias para cada aluno
# axis=1 significa que queremos a média da linha (horizontal)
colunas_notas = ['Matemática', 'Português', 'História']
df['Media_Final'] = df[colunas_notas].mean(axis=1).round(1)

# Lógica de Aprovação (Média >= 7)
# Usamos uma função lambda simples para definir o Status
df['Status'] = df['Media_Final'].apply(lambda x: 'Aprovado' if x >= 7.0 else 'Reprovado')

print("--- Resultado Final ---")
print(df[['Nome', 'Media_Final', 'Status']])

# Filtrando apenas os reprovados para ver quem precisa de reforço
reprovados = df[df['Status'] == 'Reprovado']

if not reprovados.empty:
    print("\n--- Alunos em Recuperação ---")
    print(reprovados['Nome'].tolist())