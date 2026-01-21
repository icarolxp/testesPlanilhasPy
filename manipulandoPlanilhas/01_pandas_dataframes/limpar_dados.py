import pandas as pd
import numpy as np  

# 1. Criando DataFrame com sujeira (duplicatas e valores nulos)
dados = {
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Notebook', 'Monitor', 'Mouse'],
    'Preco': [3500.00, 50.00, np.nan, 3500.00, 1200.00, np.nan],
    'Estoque': [10, 5, 20, 10, 8, 5]
}

df = pd.DataFrame(dados)

print("--- DataFrame Sujo ---")
print(df)
print("\n" + "="*30 + "\n")

# 2. Removendo linhas duplicadas
# (Notebook aparece duas vezes com os mesmos dados)
df_sem_duplicatas = df.drop_duplicates()

# 3. Tratando valores vazios
# Preenche o preço vazio do Teclado com a média dos outros preços
# Remove linhas que ainda tenham vazios críticos (se houver)
media_precos = df_sem_duplicatas['Preco'].mean()
df_limpo = df_sem_duplicatas.copy() # Boa prática criar cópia ao modificar
df_limpo['Preco'] = df_limpo['Preco'].fillna(media_precos)

print("--- DataFrame Limpo (Sem duplicatas e Preços preenchidos) ---")
print(df_limpo.round(2))