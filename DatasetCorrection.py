# ============================================================
# Autor: Italo Marques-Monteiro
# Data: 16/11/2025
# Descrição: Script para analisar a relação entre o custo da
#             cesta básica e o salário mínimo no Brasil,
#             comparando evolução histórica, poder de compra,
#             e percentuais comprometidos da renda.
# Versão: 1.0
# Contato: https://github.com/italomarquesmonteiro
# ============================================================

import pandas as pd

# Carregar arquivos
df_cb = pd.read_csv(".github/.vscode/Dataset/Cesta-Básica.csv")
df_sm = pd.read_csv(".github/.vscode/Dataset/Salário-Mínimo.csv")

# ---- Padronizar nomes das colunas (remove espaços e acentos) ----
df_cb.columns = df_cb.columns.str.strip().str.lower()
df_sm.columns = df_sm.columns.str.strip().str.lower()

# ---- Ajuste da coluna Data para ambos ----

# Cesta básica (coluna "data")
df_cb["data"] = "01-" + df_cb["data"].astype(str).str.replace("/", "-").str.replace(".", "-")
#df_cb["data"] = pd.to_datetime(df_cb["data"], dayfirst=True, errors="coerce")

df_cb= df_cb.sort_values(
    by=["data", "cidade"],
    ascending=[True, True]
)
# Salário mínimo (coluna "data")
df_sm["data"] = "01-" + df_sm["data"].astype(str).str.replace("/", "-").str.replace(".", "-")
#df_sm["data"] = pd.to_datetime(df_sm["data"], dayfirst=True, errors="coerce")

# ---- Exibe registros que não converteram (se existirem) ----
print("\nValores inválidos em Cesta Básica:")
print(df_cb[df_cb["data"].isna()])

print("\nValores inválidos em Salário Mínimo:")
print(df_sm[df_sm["data"].isna()])

# ---- Salvar arquivos atualizados ----
df_cb.to_csv(".github/.vscode/Dataset/Cesta-Básica.csv", index=False)
df_sm.to_csv(".github/.vscode/Dataset/Salário-Mínimo.csv", index=False)

print("\nArquivos atualizados e salvos com sucesso!")
