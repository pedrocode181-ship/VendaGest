import pandas as pd 
import plotly.express as px 
import streamlit as st 

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #32CD32, #E3F2FD);
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title('Estrutura de vendas por cidade')
tabela = pd.read_csv('vendas.csv')
grafico = px.sunburst(tabela, path=['cidade', 'mercado'], values='valor', color='cidade',
                     title='Estrutura de vendas ')

st.plotly_chart(grafico)


st.write('-> Click na cidade desejada para obter mais informações')
