import pandas as pd
import plotly_express as px
import streamlit as st

st.set_page_config(layout='wide')
df = pd.read_csv('dados.csv', sep=';', decimal=',')

df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
df = df.sort_values(by='Data')

df['Mes'] = df['Data'].dt.month
df['Ano'] = df['Data'].dt.year
df['Filtro'] = df['Mes'].astype(str) + '/' + df['Ano'].astype(str)
df['Valor R$'] = pd.to_numeric(df['Valor R$'], errors='coerce')


mes = st.sidebar.selectbox('Mês', df['Filtro'].unique())
data_filtrada = df[df['Filtro'] == mes]


col1,col2 = st.columns(2)
col3, col4 = st.columns(2)

fig_date = px.bar(data_filtrada, x='Data', y='Valor R$', color='Tipo', title='Gastos por dia')
col1.plotly_chart(fig_date, use_container_width=True)

in_total = data_filtrada.groupby('Tipo')['Valor R$'].sum().reset_index()
fig_in = px.bar(data_filtrada, x='Valor R$', y='Origem',title='Entradas', orientation='h', color='Tipo')
col2.plotly_chart(fig_in, use_container_width=True)