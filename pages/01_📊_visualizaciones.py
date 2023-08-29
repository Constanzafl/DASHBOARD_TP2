import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if st.checkbox('mostrar texto'):
    st.write('hola')
    

top10= pd.read_csv('10cripto.csv')

if st.checkbox('mostrar df'):
    st.dataframe(top10)
    
if st.checkbox('vista de datos head o tail'):
    if st.button('mostrar head'):
        st.write(top10.head())
    if st.button('mostrar tail'):
        st.write(top10.tail())
        
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