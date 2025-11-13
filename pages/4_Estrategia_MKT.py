import pickle
import streamlit as st
import pandas as pd
import plotly.express as px


# Carregar os DataFrames
with open('dataframes/dataframes.pkl', 'rb') as f:
    dfs = pickle.load(f)

st.title("🎯 1.4 Estratégia de Marketing")

st.markdown(
    """
    #### Perguntas de negócio

    * Em quais regiões vale a pena expandir a rede de concessionárias?
    * Quais perfis de cliente devem ser priorizados em campanhas de marketing?
    * Existe correlação entre perfil socioeconômico e características do veículo adquirido?
    """
)

st.subheader("Taxa de penetração de mercado")

st.subheader("Segmentação de clientes por perfil")

st.subheader("ROI estimado de campanhas regionais")