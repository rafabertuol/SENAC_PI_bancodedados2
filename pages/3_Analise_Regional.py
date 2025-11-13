import pickle
import streamlit as st
import pandas as pd
import plotly.express as px


# Carregar os DataFrames
with open('dataframes/dataframes.pkl', 'rb') as f:
    dfs = pickle.load(f)

st.title("🗺️ 1.3 Análise Regional")

st.markdown(
    """
    #### Perguntas de negócio

    * Quais regiões apresentam maior volume de vendas?
    * Há diferenças significativas no preço médio entre regiões?
    * Quais concessionárias têm melhor desempenho de receita?
    """
)

st.subheader("Receita por região")

st.subheader("Ticket médio por concessionária")

st.subheader("Ranking de concessionáriasa")

st.subheader("Comparação entre regiões")