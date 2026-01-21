import pandas as pd

# Dados sobre distros Linux para o DataFrame (meu hiperfoco em distros cantando alto aqui)
dados = {
    'Distro': ['Fedora', 'Ubuntu', 'Debian', 'Arch', 'Mint'],
    'Base': ['Red Hat', 'Debian', 'Debian', 'Independente', 'Ubuntu'],
    'Gerenciador Pct': ['dnf', 'apt', 'apt', 'pacman', 'apt'],
    'Dificuldade (1-10)': [6, 3, 5, 9, 2]
}

df = pd.DataFrame(dados)

# Nome do arquivo com extensão .ODS
arquivo_ods = 'distros_linux.ods'

print(f"Criando arquivo nativo LibreOffice: {arquivo_ods}...")

try:
    df.to_excel(arquivo_ods, engine='odf', index=False)
    
    print(" Sucesso! Arquivo .ods gerado.")
    print("   Abra com 'libreoffice distros_linux.ods' no terminal ou pelo gestor de arquivos.")

except ImportError:
    print("Erro: A biblioteca 'odfpy' não está instalada.")
    print("   Rode: pip install odfpy")