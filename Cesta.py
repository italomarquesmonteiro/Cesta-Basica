# ============================================================
# Autor: Italo Marques-Monteiro
# Data: 14/11/2025
# Descrição: Script para analisar a relação entre o custo da
#             cesta básica e o salário mínimo no Brasil,
#             comparando evolução histórica, poder de compra,
#             e percentuais comprometidos da renda.
# Versão: 1.0
# Contato: https://github.com/italomarquesmonteiro
# ============================================================


import pandas as pd

# --- 1. Ler o arquivo CSV ---
cesta = pd.read_csv(".github/.vscode/Dataset/Cesta-Básica.csv")

print("Formato original (wide):")
print(cesta.head())

# --- 2. Converter de largo → longo mantendo “Mês-Ano” como ID ---
df_long = cesta.melt(
    id_vars=["data"],   
    var_name="Cidade",
    value_name="Valor_Cesta"
)

# --- 3. Ordenar por data DESC e cidade ASC ---
df_long = df_long.sort_values(
    by=["data", "Cidade"],
    ascending=[False, True]
)

print("\nFormato convertido (long):")
print(df_long.head())

# --- 3. Salvar ---
df_long.to_csv(".github/.vscode/Dataset/Cesta-Básica-Long.csv", index=False)

print(f"\nArquivo salvo em: {df_long}")