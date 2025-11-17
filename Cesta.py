# ============================================================
# Autor: Italo Marques-Monteiro
# Data: 14/11/2025
# Descrição: Script para analisar a relação entre o custo da
#             cesta básica e o salário mínimo no Brasil,
#             comparando evolução histórica, poder de compra,
#             e percentuais comprometidos da renda.
# Versão: 1.2 (corrigida com Font Awesome funcional)
# Contato: https://github.com/italomarquesmonteiro
# ============================================================

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================
# ÍCONES (unicode + estilo correto)
# =========================
github_icon    = "<span style='font-family:\"Font Awesome 6 Brands\"; font-weight:400;'>&#xf09b;</span>"
linkedin_icon  = "<span style='font-family:\"Font Awesome 6 Brands\"; font-weight:400;'>&#xf0e1;</span>"
x_icon         = "<span style='font-family:\"Font Awesome 6 Brands\"; font-weight:400;'>&#xf099;</span>"
instagram_icon = "<span style='font-family:\"Font Awesome 6 Brands\"; font-weight:400;'>&#xf16d;</span>"

github_user    = "italomarquesmonteiro"
linkedin_user  = "italomarquesmonteiro"
x_user         = "italommonteiro"
instagram_user = "italo.m.m"

# =========================
# 1. Ler arquivos CSV
# =========================
cesta = pd.read_csv(".github/.vscode/Dataset/Cesta-Básica.csv")
salario = pd.read_csv(".github/.vscode/Dataset/Salário-Mínimo.csv")

# =========================
# 2. Preparar dados
# =========================
cesta['data'] = pd.to_datetime(cesta['data'], format="%d-%m-%Y")
cesta['ano_mes'] = cesta['data'].dt.to_period('M')
media_mensal = cesta.groupby('ano_mes')['custo'].mean().round(2).reset_index()

salario['data'] = pd.to_datetime(salario['data'], format="%d-%m-%Y")
salario['ano_mes'] = salario['data'].dt.to_period('M')

df_final = media_mensal.merge(salario[['ano_mes', 'valor']], on='ano_mes', how='inner')
df_final = df_final[df_final['ano_mes'] >= pd.Period('1994-07', freq='M')]
df_final['poder_de_compra'] = (df_final['valor'] / df_final['custo']).round(2)
df_final['ano_mes'] = df_final['ano_mes'].astype(str)

# =========================
# Título e Créditos
# =========================
TITULO = (
    "<span style='font-size:23px; font-weight:600;'>"
    "Poder de Compra do Salário Mínimo no Brasil"
    "</span>"
)

SUBTITULO = (
    "<span style='font-size:14px; font-weight:400; color:#c7c7c7;'>"
    "Evolução do número de cestas básicas que podem ser adquiridas com 1 salário mínimo.<br>"
    "De jul/1994 (1,02 cesta) até 2025, o poder de compra chega a aproximadamente 2,19 cestas."
    "</span>"
)

CREDITOS = (
    "<span style='font-size:11px; color:#929292;'>"
    "<b>Fonte:</b> DIEESE — média de 17 capitais brasileiras.<br>"
    "<b>Visualização:</b> Ítalo Marques Monteiro<br><br>"
    f"{github_icon} {github_user} &nbsp;&nbsp; "
    f"{linkedin_icon} {linkedin_user} &nbsp;&nbsp; "
    f"{x_icon} {x_user} &nbsp;&nbsp; "
    f"{instagram_icon} {instagram_user}"
    "</span>"
)

# =========================
# Gráfico Interativo Dark
# =========================
fig = px.line(
    df_final, x="ano_mes", y="poder_de_compra",
    hover_data=["valor", "custo"]
)

fig.update_traces(line=dict(width=3), mode="lines")
fig.update_layout(
    template="plotly_dark",
    title=dict(text=TITULO + "<br><sup>" + SUBTITULO + "</sup>", x=0.02),
    xaxis_title="Ano / Mês",
    yaxis_title="Cestas Básicas",
    hovermode="x unified",
    margin=dict(l=60, r=60, t=120, b=160),
    font=dict(family="Arial", size=13, color="#E0E0E0")
)

# Faixa da Pandemia
fig.add_vrect(
    x0="2020-03", x1="2022-12",
    fillcolor="red", opacity=0.14,
    layer="below", line_width=0,
    annotation_text="Pandemia COVID-19",
    annotation_position="top left",
    annotation_font_color="red"
)

# Créditos (anotação inferior)
fig.add_annotation(
    text=CREDITOS, showarrow=False,
    xref="paper", yref="paper",
    x=0, y=-0.18, align="left"
)

fig.show()

# =========================
# Exportação — HTML com Font Awesome habilitado
# =========================
extra_header = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
"""

with open("poder_de_compra_interativo.html", "w", encoding="utf-8") as f:
    f.write(extra_header + fig.to_html(include_plotlyjs="cdn", full_html=False))

print("Arquivo salvo com sucesso com ícones funcionais!")

