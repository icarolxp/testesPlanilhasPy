import pandas as pd
import random

nomes_base = ['joão', 'maria', 'pedro', 'ana', 'carlos', 'lucia', 'bruno']
sobrenomes = ['silva', 'souza', 'almeida', 'santos', 'oliveira']
dominios = ['email.com', 'teste.com.br', 'empresa.net']

dados = []
for _ in range(50):
    # Bagunçando os nomes 
    nome = f"{random.choice(nomes_base)} {random.choice(sobrenomes)}"
    if random.random() > 0.5:
        nome = nome.upper() # ALGUNS EM CAIXA ALTA
    if random.random() > 0.3:
        nome = f"  {nome}  " # Adicionando espaços extras
        
    email = f"{nome.strip().lower().replace(' ', '.')}@{random.choice(dominios)}"
    
    dados.append({'Nome_Bruto': nome, 'Email': email})

df = pd.DataFrame(dados)

print("Dados Originais")
print(df.head())

# LIMPEZA
# 1. Padronizar: Remove espaços e coloca em Título (João Silva)
df['Nome_Formatado'] = df['Nome_Bruto'].str.strip().str.title()

# 2. Extrair Provedor do Email
df['Provedor'] = df['Email'].str.split('@').str[1]

# 3. Filtrar quem tem 'Silva'
tem_silva = df[df['Nome_Formatado'].str.contains('Silva')]

print("\nDados Tratados")
print(df[['Nome_Bruto', 'Nome_Formatado', 'Provedor']].head())

print(f"\nTotal de pessoas 'Silva' encontradas: {len(tem_silva)}")