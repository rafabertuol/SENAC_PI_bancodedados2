import pickle
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px


# Carregar os DataFrames
with open('dataframes/dataframes.pkl', 'rb') as f:
    dfs = pickle.load(f)

st.title("🚗 1.1 Vendas e Desempenho Comercial")

# Usar os DataFrames
col1, col2, col3 = st.columns(3)

# Total de Vendas (valor direto)
col1.metric(
    "Total de Vendas",
    f"{int(dfs['df_total']['Valor'][0]):,}".replace(",", ".")
)

# Receita Total
df_receita = dfs['df_receita_total']  # acessa o DataFrame correto
col2.metric(
    "Receita Total",
    f"${(df_receita.loc[df_receita['Métrica'] == 'Receita Total', 'Valor'].values[0]):,.2f}"
    .replace(",", "X").replace(".", ",").replace("X", ".")
)

# Ticket Médio
col3.metric(
    "Ticket Médio",
    f"${(df_receita.loc[df_receita['Métrica'] == 'Ticket Médio', 'Valor'].values[0]):,.2f}"
    .replace(",", "X").replace(".", ",").replace("X", ".")
)

st.subheader("Modelos e marcas mais vendidos")
st.dataframe(dfs['df_modelos_vendidos'].head(10))

# Share por quantidade vendida
st.subheader("Share por quantidade vendida")
df_modelos = dfs['df_modelos_vendidos']

# Agrupa por marca e soma a quantidade
df_share_marca = (
    df_modelos.groupby('Marca', as_index=False)['Quantidade']
    .sum()
)

# Calcula o percentual de participação
df_share_marca['Share (%)'] = (
    df_share_marca['Quantidade'] / df_share_marca['Quantidade'].sum() * 100
)

# Ordena do maior para o menor
df_share_marca = df_share_marca.sort_values(by='Share (%)', ascending=False)

st.dataframe(df_share_marca)

# Share por receita total
st.subheader("Share por receita total")

df_share_receita = (
    df_modelos.groupby('Marca', as_index=False)['Receita Total']
    .sum()
)
df_share_receita['Share Receita (%)'] = (
    df_share_receita['Receita Total'] / df_share_receita['Receita Total'].sum() * 100
)
# Ordenar do maior para o menor
df_share_receita = df_share_receita.sort_values(by='Share Receita (%)', ascending=False)

st.dataframe(df_share_receita)

# Criar gráfico de barras horizontais
st.markdown("#### 📊 Participação de Receita por Marca")
fig = px.bar(
    df_share_receita,
    x='Share Receita (%)',
    y='Marca',
    orientation='h',
    text=df_share_receita['Share Receita (%)'].apply(lambda x: f"{x:.1f}%")
)

# Ajustar layout
fig.update_traces(textposition='outside')
fig.update_layout(
    xaxis_title="Participação (%)",
    yaxis_title="Marca",
    title_x=0.3,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
)

st.plotly_chart(fig, use_container_width=True)

#####################
#   Gráfico de Linhas - Taxa de Crescimento
#####################

st.markdown("#### 📊 Taxa de Crescimento")
st.line_chart(dfs['df_vendas_mes'].set_index('Mês')['Receita'])

#####################
#   Gráfico de Pizza - Participação por Marca
#####################

# Paleta personalizada (10 cores)
cores = [
    "#3A7DFF",  # azul forte
    "#FF6FB1",  # rosa
    "#00A676",  # verde
    "#F4A259",  # laranja suave
    "#8D5B4C",  # marrom elegante
    "#6A4C93",  # roxo
    "#D4A017",  # dourado
    "#FF4F4F",  # vermelho claro
    "#0096C7",  # azul petróleo
    "#8ECae6"   # azul claro
]
st.markdown("#### Participação por Marca — Quantidade Vendida")
fig = px.pie(
    dfs["df_top_marcas"],
    names="Marca",
    values="Quantidade",
    hole=0.45,
    color="Marca",
    color_discrete_sequence=cores
)

fig.update_traces(
    textinfo="percent",
    pull=[0.03] * len(dfs["df_top_marcas"]),  # efeito de leve destaque
    hovertemplate="<b>%{label}</b><br>" +
                  "Quantidade: %{value}<br>" +
                  "Receita Total: R$ %{customdata}<extra></extra>",
    customdata=dfs["df_receita_total"]
)

fig.update_layout(
    showlegend=True,
    legend_title="Marca",
    template="plotly_white",
    margin=dict(t=60, b=20, l=20, r=20),
)

st.plotly_chart(fig, use_container_width=True)