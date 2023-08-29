import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Top 10 de criptomonedas por capitalizacion de mercado')
st.markdown('*****')


if st.checkbox('¿Por qué capitalización de mercado?'):
    st.write('La capitalización de mercado es un indicador clave que refleja el valor total de una criptomoneda en circulación en función de su precio actual. Es calculada multiplicando el precio actual de cada token por su oferta circulante. A través de este enfoque, podemos comprender la valoración relativa de cada token en comparación con otros en el mismo mercado.')
    if st.button('MARKET-CAP'):
        st.write('**Capitalizacion de mercado= Precio de activo digital * volument total circulante**')

top10= pd.read_csv('10cripto.csv')
top10['ath_date']= pd.to_datetime(top10['ath_date'])
top10['atl_date']=pd.to_datetime(top10['atl_date'])

if st.checkbox('Data Frame top 10 monedas *FECHA=21/08/2023*'):
    st.dataframe(top10)
    
if st.checkbox('Grafico de barras'):
    if st.button('Top 10 capitalizacion de mercado'):
        fig=plt.figure(figsize=(6,4))
        plt.barh( top10['name'],top10['market_cap'], color='blue')
        plt.xlabel('USD')
        plt.ylabel('Criptomoneda')
        plt.title('Capitalizacion de mercado')
        st.pyplot(fig)
    if st.button('Volumen total de criptomonedas'):
        fig= plt.figure(figsize=(6,4))
        plt.barh( top10['name'],top10['total_volume'], color='pink')
        plt.xlabel('Volumen')
        plt.ylabel('Criptomoneda')
        plt.title('Volumen total de criptomonedas')
        st.pyplot(fig)

dim= st.radio('Dimensión a mostrar:', ('Filas', 'Columnas'))

if dim == 'Filas':
    st.write('Cantidad de filas:', top10.shape[0])
if dim == 'Columnas':
    st.write('Cantidad de columnas:', top10.shape[1])
    
precio_limite = st.slider('definir precio máximo', 0,4000, 70000)

fig= plt.figure(figsize=(6,4))
sns.scatterplot(x='ath', y='name', data = top10[top10['ath']<precio_limite])
st.pyplot(fig)

criptomonedas= top10['name'].unique().tolist()
eleccion_cripto= st.multiselect('seleccione una criptomoneda:', criptomonedas, default=['Bitcoin','BNB'])
df_eleccion= top10[top10['name'].isin(eleccion_cripto)]

fig= plt.figure(figsize=(6,4))
sns.scatterplot(x='ath', y='name',data = df_eleccion) #puedo agregar hue
st.pyplot(fig)


col1, col2 = st.columns(2)
with col1:
    top10= top10[top10['name']=='Bitcoin']
    fig=plt.figure()
    sns.scatterplot(x='ath', y='name', data=top10)
    plt.title('valor maximo bitcoin')
    st.pyplot(fig)
with col2:
    top10= top10[top10['name']=='BNB']
    fig=plt.figure()
    sns.scatterplot(x='ath', y='name', data=top10)
    plt.title('valor maximo bnb')
    st.pyplot(fig)