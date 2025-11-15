import pickle
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from numpy.random import default_rng as rng

# Carregar os DataFrames
with open('dataframes/dataframes.pkl', 'rb') as f:
    dfs = pickle.load(f)

st.title("👤 1.2 Perfil Cliente")

st.markdown(
    """
    #### Perguntas de negócio

    * **Clientes de maior renda compram quais tipos de veículos?**
    * **Existe diferença de preferência entre homens e mulheres?**
    * **Qual é a faixa de renda predominante dos compradores em cada região?**
    """
)

st.subheader("Distribuição de clientes por faixa de renda")

# Gráfico de barras
chart = (
    alt.Chart(dfs["df_agrupar_faixa_renda"])
    .mark_bar()
    .encode(
        x=alt.X("Faixa de Renda:N", sort="-y"),
        y=alt.Y("Quantidade:Q"),
        tooltip=["Faixa de Renda", "Quantidade", "Preço Médio", "Renda Média", "Percentual (%)"]
    )
    .properties(
        width="container"
    )
)
st.altair_chart(chart, use_container_width=True)

st.subheader("Percentual de vendas por gênero")

# Gráfico de Pizza
chart = alt.Chart(dfs["df_genero"]).mark_arc().encode(
    theta=alt.Theta(field="Percentual (%)", type="quantitative"),
    color=alt.Color(field="Gênero", type="nominal"),
    tooltip=["Gênero", "Percentual (%)"]
)

st.altair_chart(chart, use_container_width=True)


st.subheader("Relação renda × modelo de veículo")





st.subheader("Preferências por renda e gênero")

# ================================
# GRÁFICO 1 — Scatter com gênero
# ================================
jitter1 = alt.Chart(dfs["df_preferencias"]).transform_calculate(
    jitter="(random() - 0.5) * 0.3"
)

chart_scatter_genero = (
    jitter1.mark_circle(size=120, opacity=0.7)
    .encode(
        x=alt.X("Quantidade:Q", title="Quantidade"),
        y=alt.Y("Marca:N", title="Marca"),
        color=alt.Color(
            "Gênero:N",
            scale=alt.Scale(
                domain=["Male", "Female"],
                range=["#3A7DFF", "#FF6FB1"],  # azul / rosa
            ),
            title="Gênero",
        ),
        tooltip=[
            "Gênero",
            "Marca",
            "Faixa de Renda",
            "Quantidade",
            "Preço Médio",
        ],
    )
)

# ===========================================
# GRÁFICO 2 — Scatter com faixa de renda
# ===========================================
jitter2 = alt.Chart(dfs["df_preferencias"]).transform_calculate(
    jitter="(random() - 0.5) * 0.3"
)

color_scale = alt.Scale(
    domain=[
        "Alta (> 1M)",
        "Média-Alta (500k-1M)",
        "Média (100k-500k)",
        "Baixa (< 50k)",
    ],
    range=["#3A7DFF", "#005C40", "#EC4899", "#D4A017"],
)

chart_scatter_renda = (
    jitter2.mark_circle(size=150, opacity=0.75)
    .encode(
        x=alt.X("Quantidade:Q", title="Quantidade"),
        y=alt.Y("Marca:N", title="Marca", sort="-x"),
        color=alt.Color("Faixa de Renda:N", scale=color_scale, title="Faixa de Renda"),
        tooltip=[
            "Faixa de Renda",
            "Gênero",
            "Marca",
            "Quantidade",
            "Preço Médio",
        ],
    )
)

# =============================
# LAYOUT EM 2 COLUNAS
# =============================
col1, col2 = st.columns([2, 2])  # 50/50

col1.write("Preferências por Gênero")
col1.altair_chart(chart_scatter_genero, use_container_width=True)

col2.write("Preferências por Faixa de Renda")
col2.altair_chart(chart_scatter_renda, use_container_width=True)