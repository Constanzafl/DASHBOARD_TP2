import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Top 10 de criptomonedas por capitalización de mercado')
st.markdown('*****')

st.write('**Elegimos 10 monedas teniendo en cuenta como parámetro, la capitalización de mercado en orden descendente.**')

if st.checkbox('¿Por qué elegimos capitalización de mercado?'):
    st.write('La capitalización de mercado es un indicador clave que refleja el valor total de una criptomoneda en circulación en función de su precio actual. Es calculada multiplicando el precio actual de cada token por su oferta circulante. A través de este enfoque, podemos comprender la valoración relativa de cada token en comparación con otros en el mismo mercado.')
    if st.button('MARKET-CAP'):
        st.write('**Capitalizacion de mercado= Precio de activo digital * volument total circulante**')

top10= pd.read_csv('10cripto.csv')
top10['ath_date']= pd.to_datetime(top10['ath_date']).dt.date
top10['atl_date']=pd.to_datetime(top10['atl_date']).dt.date

if st.checkbox('Data Frame top 10 monedas, obtenido de la fuentes de información de CoinGecko'):
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

if st.checkbox('Correlacion entre precio, market cap y volumen de criptomonedas'):
    if st.button('Mapa de calor'):
        top10mkt= top10[['market_cap', 'total_volume', 'current_price']]
        fig=plt.figure(figsize=(6,4))
        sns.heatmap(top10mkt.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Gráfico de Correlación entre Capitalización de Mercado y Volumen Total')
        st.pyplot(fig)
    
st.write('#### Precios actuales de las 10 Criptomonedas con mayor capitalización de mercado')        
fig= plt.figure(figsize=(5,5))
precio_limite = st.slider('Cripto segun precio', 0,4000, 30000)
sns.scatterplot(data=top10[top10['current_price']<precio_limite], x='current_price',y='name', color='red')
plt.xlabel('Precio en USD')
plt.ylabel('Nombre')
st.pyplot(fig)    

st.write('### Valores máximos historicos')
criptomonedas= top10['name'].unique().tolist()
eleccion_cripto= st.multiselect('Seleccione una o mas criptomonedas:', criptomonedas, default=['Bitcoin','Ethereum'])
df_eleccion= top10[top10['name'].isin(eleccion_cripto)]

fig= plt.figure(figsize=(6,4))
sns.scatterplot(x='ath', y='name',data = df_eleccion, color='purple') #puedo agregar hue
st.pyplot(fig)

dim= st.radio('Valores máximos históricos en USD:', ('Bitcoin', 'Ethereum', 'Tether USD', 'BNB', 'XRP', 'USD Coin',
                                              'Lido', 'Cardano', 'Solana', 'Doge Coin'))

if dim == 'Bitcoin':
    st.write('FECHA:', top10.iloc[0][14], 'Valor:', top10.iloc[0][12])
if dim == 'Ethereum':
    st.write('Fecha:', top10.iloc[1][14], 'Valor:', top10.iloc[1][12])
if dim == 'Tether USD':
    st.write('Fecha:', top10.iloc[2][14], 'Valor:', top10.iloc[2][12])
if dim == 'BNB':
    st.write('Fecha:', top10.iloc[3][14], 'Valor:', top10.iloc[3][12])
if dim == 'XRP':
    st.write('Fecha:', top10.iloc[4][14], 'Valor:', top10.iloc[4][12])
if dim == 'USD Coin':
    st.write('Fecha:', top10.iloc[5][14], 'Valor:', top10.iloc[5][12])
if dim == 'Lido':
    st.write('Fecha:', top10.iloc[6][14], 'Valor:', top10.iloc[6][12])
if dim == 'Cardano':
    st.write('Fecha:', top10.iloc[7][14], 'Valor:', top10.iloc[7][12])
if dim == 'Solana':
    st.write('Fecha:', top10.iloc[8][14], 'Valor:', top10.iloc[8][12])
if dim == 'Doge Coin':
    st.write('Fecha:', top10.iloc[9][14], 'Valor:', top10.iloc[9][12])
    

st.write('### Valores mínimos historicos')
fig= plt.figure(figsize=(6,4))
sns.scatterplot(x='atl', y='name',data = df_eleccion, color='black') 
st.pyplot(fig)

dim= st.radio('Valores mínimos históricos en USD:', ('Bitcoin', 'Ethereum', 'Tether USD', 'BNB', 'XRP', 'USD Coin',
                                              'Lido', 'Cardano', 'Solana', 'Doge Coin'))
if dim == 'Bitcoin':
    st.write('Fecha:', top10.iloc[0][17], 'Valor:', top10.iloc[0][15])
if dim == 'Ethereum':
    st.write('Fecha:', top10.iloc[1][17], 'Valor:', top10.iloc[1][15])
if dim == 'Tether USD':
    st.write('Fecha:', top10.iloc[2][17], 'Valor:', top10.iloc[2][15])
if dim == 'BNB':
    st.write('Fecha:', top10.iloc[3][17], 'Valor:', top10.iloc[3][15])
if dim == 'XRP':
    st.write('Fecha:', top10.iloc[4][17], 'Valor:', top10.iloc[4][15])
if dim == 'USD Coin':
    st.write('Fecha:', top10.iloc[5][17], 'Valor:', top10.iloc[5][15])
if dim == 'Lido':
    st.write('Fecha:', top10.iloc[6][17], 'Valor:', top10.iloc[6][15])
if dim == 'Cardano':
    st.write('Fecha:', top10.iloc[7][17], 'Valor:', top10.iloc[7][15])
if dim == 'Solana':
    st.write('Fecha:', top10.iloc[8][17], 'Valor:', top10.iloc[8][15])
if dim == 'Doge Coin':
    st.write('Fecha:', top10.iloc[9][17], 'Valor:', top10.iloc[9][15])
