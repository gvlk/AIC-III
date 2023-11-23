import streamlit as st
import pandas as pd

# para colocar o dashboard no ar usar o comando: streamlit run dashboards.py

st.set_page_config(page_title='Dashboard')

with st.container():
    st.title('Valores por dia')
    st.write('Para visão personalizada, utilize os filtros')

with st.container():
    st.write('Saídas')
    df_out = pd.read_csv('dadosout.csv', sep=';', decimal=',')
    st.line_chart(df_out, y='Valor R$', x='Data', color='#FF0000')

with st.container():
    st.write('Entradas')
    df_in = pd.read_csv('dadosin.csv', sep=';', decimal=',')
    st.line_chart(df_in, y='Valor R$', x='Data', color='#0000FF')
