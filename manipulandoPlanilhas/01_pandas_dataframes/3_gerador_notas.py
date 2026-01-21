import pandas as pd
import random

# Listas para sortear nomes e sobrenomes
nomes = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Julia']
sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Pereira', 'Lima', 'Ferreira', 'Costa']

dados = []

# Gerando 50 alunos com notas aleatórias
for _ in range(50):
    # Escolhe um nome e um sobrenome aleatórios
    nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
    
    # Gera notas aleatórias entre 0.0 e 10.0 (arredondadas para 1 casa decimal)
    # A função uniform gera números "quebrados" (floats)
    aluno = {
        'Nome': nome_completo,
        'Matemática': round(random.uniform(0.0, 10.0), 1),
        'Português': round(random.uniform(0.0, 10.0), 1),
        'História': round(random.uniform(0.0, 10.0), 1)
    }
    dados.append(aluno)

df = pd.DataFrame(dados)

# Salvando o arquivo
df.to_csv('notas_escolares.csv', index=False)
print(f"Sucesso! Arquivo 'notas_escolares.csv' criado com {len(df)} alunos.")