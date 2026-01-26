import pandas as pd
import random

# Listas para sorteio
generos = ['Sci-Fi', 'Romance', 'Ação', 'Crime', 'Animação', 'Comédia', 'Terror']
anos = range(1980, 2025)

dados = []
for i in range(100):
    dados.append({
        'Filme': f'Filme_{i+1:03d}', # Gera Filme_001, Filme_002...
        'Ano': random.choice(anos),
        'Nota': round(random.uniform(1.0, 10.0), 1),
        'Genero': random.choice(generos)
    })

df = pd.DataFrame(dados)

print("Amostra do Catálogo (5 primeiros)")
print(df.head())

# 1. Filtro: Sci-Fi com nota alta (> 8.0)
filtro1 = df[(df['Genero'] == 'Sci-Fi') & (df['Nota'] > 8.0)]

# 2. Query: Filmes recentes (> 2020) OU que sejam Crime
filtro2 = df.query('Ano > 2020 or Genero == "Crime"')

print(f"\nSci-Fi de Alta Nota ({len(filtro1)} encontrados) ")
print(filtro1.head()) # Mostra só o começo do resultado
print(f"\nRecentes ou Crime ({len(filtro2)} encontrados)  ")
print(filtro2[['Filme', 'Ano', 'Genero']].head())