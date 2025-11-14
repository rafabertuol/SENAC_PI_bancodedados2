import pickle
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px


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


st.subheader("Relação renda × modelo")
chart = (
    alt.Chart(dfs["df_renda_x_modelo"])
    .mark_bar()
    .encode(
        y=alt.Y("Modelo:N", title="Modelo"),
        x=alt.X("sum(Quantidade):Q", title="Quantidade Total"),
        color=alt.Color("Faixa de Renda:N", title="Faixa de Renda"),
        tooltip=[
            "Faixa de Renda",
            "Modelo",
            "Quantidade",
            "Preço Médio",
            "Esforço Financeiro"
        ]
    )
)

st.altair_chart(chart, use_container_width=True)

st.subheader("Preferências por renda e gênero")

# preferencia por genero
jitter = alt.Chart(dfs["df_preferencias"]).transform_calculate(
    jitter="(random() - 0.5) * 0.3"
)

chart_scatter = (
    jitter.mark_circle(size=120, opacity=0.7)
    .encode(
        x=alt.X("Quantidade:Q", title="Quantidade"),
        y=alt.Y("Marca:N", title="Marca"),
        color=alt.Color(
            "Gênero:N",
            scale=alt.Scale(
                domain=["Male", "Female"],
                range=["#3A7DFF", "#FF6FB1"]   # azul / rosa
            ),
            title="Gênero"
        ),
        tooltip=[
            "Gênero",
            "Marca",
            "Faixa de Renda",
            "Quantidade",
            "Preço Médio"
        ]
    )
)

st.altair_chart(chart_scatter, use_container_width=True)

# preferencia por renda 
# Jitter para espalhar os pontos
jitter = alt.Chart(dfs["df_preferencias"]).transform_calculate(
    jitter="(random() - 0.5) * 0.3"
)

# Definição da paleta de 4 cores
color_scale = alt.Scale(
    domain=[
        "Alta (> 1M)", 
        "Média-Alta (500k-1M)",
        "Média (100k-500k)",
        "Baixa (< 50k)"
    ],
    range=[
        "#3A7DFF",  # Azul forte
        "#005C40",  # verde escuro 
        "#EC4899",  # Rosa forte
        "#D4A017"   # dourado
    ]
)

chart_scatter = (
    jitter.mark_circle(size=150, opacity=0.75)
    .encode(
        x=alt.X("Quantidade:Q", title="Quantidade"),
        y=alt.Y("Marca:N", title="Marca", sort="-x"),
        color=alt.Color(
            "Faixa de Renda:N",
            scale=color_scale,
            title="Faixa de Renda"
        ),
        tooltip=[
            "Faixa de Renda",
            "Gênero",
            "Marca",
            "Quantidade",
            "Preço Médio"
        ]
    )
)

st.altair_chart(chart_scatter, use_container_width=True)