"""
============================================================================
PROJETO INTEGRADOR - APOIO DECISÓRIO AOS NEGÓCIOS
Script da Seção 1.1 - Perfil Cliente
Autor: Aline Morais
Data: 14/11/2025
Descrição: Script Python para utilizar o streamlit
============================================================================
"""

import pickle
import streamlit as st
import plotly.express as px
import altair as alt

# Carregar os DataFrames
with open('dataframes/dataframes.pkl', 'rb') as f:
    dfs = pickle.load(f)

st.title("🗺️ 1.3 Análise Regional")

# ================================
# GRÁFICO 1 — Barra horizontal receita por região
# ================================
st.subheader("📊 Receita por região")

chart_regiao = (
    alt.Chart(dfs["df_receita_regiao"])
    .mark_bar(size=40)
    .encode(
        x=alt.X("Receita Total:Q", title="Receita Total (R$)"),
        y=alt.Y("Região:N", sort="-x"),
        color=alt.Color("Região:N", legend=None),
        tooltip=["Região", "Receita Total", "Quantidade", "Percentual (%)"]
    )
)

st.altair_chart(chart_regiao, use_container_width=True)

# ================================
# GRÁFICO 2 — Barra horizontal ticket médio por região e tabela de top 5
# ================================
st.subheader("📈 Ticket Médio por Concessionária")
df_receita_regiao = dfs["df_receita_regiao"]  # <-- nome certo

df_receita_regiao["Ticket Médio"] = (
    df_receita_regiao["Receita Total"] / df_receita_regiao["Quantidade"]
).round(2)

chart_ticket = (
    alt.Chart(df_receita_regiao)
    .mark_bar(size=40)
    .encode(
        x=alt.X("Ticket Médio:Q", title="Ticket Médio (R$)"),
        y=alt.Y("Região:N", sort="-x"),
        color=alt.Color("Região:N", legend=None),
        tooltip=[
            "Região",
            "Ticket Médio",
            "Quantidade",
            "Receita Total",
        ],
    )
)

col1, col2 = st.columns([2, 1])

with col1:
    st.write("Ranking de Ticket Médio")
    st.altair_chart(chart_ticket, use_container_width=True)

with col2:
    st.write("Top 5 Ticket Médio")
    st.dataframe(
        df_receita_regiao[["Região", "Ticket Médio"]]
        .sort_values("Ticket Médio", ascending=False)
        .head(5)
    )

# ================================
# GRÁFICO 3 - Ranking de concessionárias
# ================================
st.subheader("📈  Ranking de concessionárias")
heatmap_ranking = (
    alt.Chart(dfs["df_ranking"])
    .mark_rect()
    .encode(
        y=alt.Y("Concessionária:N", sort=alt.SortField("Ranking", order="ascending")),
        x=alt.X("Ranking:O", title="Ranking"),
        color=alt.Color(
            "Ranking:Q",
            scale=alt.Scale(scheme="viridis", reverse=True),
            title="Ranking"
        ),
        tooltip=[
            "Ranking",
            "Concessionária",
            "Região",
            "Quantidade",
            "Receita Total"
        ]
    )
).properties(
    height=300,
    width="container"
)

st.markdown("##### 🏆 Ranking de Concessionárias")

# tabela mantida

st.dataframe(
    dfs["df_ranking"][[
        "Ranking",
        "Concessionária",
        "Região",
        "Quantidade",
        "Receita Total"
    ]].sort_values("Ranking").head(10)
)

st.markdown("##### 🔥 Mapa de Calor — Receita por Concessionária")
st.altair_chart(heatmap_ranking, use_container_width=True)


st.subheader("📊 Comparação entre Regiões")

# ================================
#GRÁFICO 4 — Receita por Concessionária
# ================================
st.markdown("#### Receita por Concessionária (Top Regiões)")
fig_bar = px.bar(
    dfs["df_comparacao_regioes"].sort_values("Receita por Concessionária", ascending=False),
    x="Receita por Concessionária",
    y="Região",
    orientation="h",
    text_auto=".2s",
    template="plotly_white",
)
st.plotly_chart(fig_bar, use_container_width=True)


# ================================
# GRÁFICO 5 — Ticket Médio vs Receita por Concessionária
# ================================
st.subheader("📊 Comparação Direta de Indicadores")
df_melt = dfs["df_comparacao_regioes"].melt(
    id_vars="Região",
    value_vars=["Ticket Médio", "Receita por Concessionária"],
    var_name="Métrica",
    value_name="Valor"
)

fig_grouped = px.bar(
    df_melt,
    x="Região",
    y="Valor",
    color="Métrica",
    barmode="group",
    template="plotly_white",
    text_auto=".2s"
)
st.plotly_chart(fig_grouped, use_container_width=True)