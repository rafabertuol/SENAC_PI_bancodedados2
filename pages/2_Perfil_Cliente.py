import pickle
import streamlit as st
import pandas as pd
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



st.subheader("Percentual de vendas por gênero")



st.subheader("Índice de esforço financeiro")