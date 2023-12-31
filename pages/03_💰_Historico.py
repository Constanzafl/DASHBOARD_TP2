import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Valores históricos de las criptomonedas desde el año 2020 hasta la actualidad')
st.markdown('*****')

bitcoin= pd.read_csv('bitcoinDB.csv')
bnb= pd.read_csv('bnbDB.csv')
car= pd.read_csv('bnbDB.csv')
doge= pd.read_csv('dogecoinDB.csv')
eter= pd.read_csv('ethereumDB.csv')
lido= pd.read_csv('lidoDB.csv')
sol=pd.read_csv('solDB.csv')
teter= pd.read_csv('tetherDB.csv')
usd=pd.read_csv('usdDB.csv')
xrp=pd.read_csv('xrpDB.csv')

st.write('**Haciendo click en la siguiente cuadrícula, podras ver los gráficos correspondientes a cada moneda con precio, capitalización de mercado y trading volume**')
bitcoin['FECHAS']=pd.to_datetime(bitcoin['FECHAS'])
bnb['FECHAS']=pd.to_datetime(bnb['FECHAS'])
car['FECHAS']=pd.to_datetime(car['FECHAS'])
doge['FECHAS']=pd.to_datetime(doge['FECHAS'])
eter['FECHAS']=pd.to_datetime(eter['FECHAS'])
lido['FECHAS']=pd.to_datetime(lido['FECHAS'])
sol['FECHAS']=pd.to_datetime(sol['FECHAS'])
teter['FECHAS']=pd.to_datetime(teter['FECHAS'])
usd['FECHAS']=pd.to_datetime(usd['FECHAS'])
xrp['FECHAS']=pd.to_datetime(xrp['FECHAS'])

if st.checkbox('BITCOIN'):
    st.markdown('Bitcoin es la primera y más reconocida criptomoneda. Fue creado como una alternativa a las monedas fiduciarias tradicionales y es considerado por muchos como una reserva de valor digital. Su oferta limitada y la adopción institucional han contribuido a su crecimiento y legitimidad en los mercados financieros.')
    fig1= plt.figure(figsize=(10, 6))
    plt.plot(bitcoin['FECHAS'], bitcoin['PRECIO-usd'], label='Precio de Cierre', color='blue')
    plt.xlabel('Fecha')
    plt.ylabel('Precio USD')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig1)
    
    
    fig2= plt.figure(figsize=(10, 6))
    plt.plot(bitcoin['FECHAS'], bitcoin['MARKET_CAP-usd'], label='market cap', color='red')
    plt.xlabel('Fecha')
    plt.ylabel('Market Cap')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig2)
    
    
    fig3= plt.figure(figsize=(10, 6))
    plt.plot(bitcoin['FECHAS'], bitcoin['TOTAL_VOLUMES'], label='volumen', color='orange')
    plt.xlabel('Fecha')
    plt.ylabel('Volume')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig3)
      



if st.checkbox('Ethereum'):
    st.markdown('Ethereum es una plataforma de contratos inteligentes y aplicaciones descentralizadas. Es conocido por impulsar el auge de las finanzas descentralizadas (DeFi) y los tokens no fungibles (NFT), transformando la forma en que se construyen y utilizan aplicaciones en línea.')
    fig1= plt.figure(figsize=(10, 6))
    plt.plot(eter['FECHAS'], eter['PRECIO-usd'], label='Precio de Cierre', color='blue')
    plt.xlabel('Fecha')
    plt.ylabel('Precio USD')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig1)
    
    
    fig2= plt.figure(figsize=(10, 6))
    plt.plot(eter['FECHAS'], eter['MARKET_CAP-usd'], label='market cap', color='red')
    plt.xlabel('Fecha')
    plt.ylabel('Market Cap')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig2)
    
    
    fig3= plt.figure(figsize=(10, 6))
    plt.plot(eter['FECHAS'], eter['TOTAL_VOLUMES'], label='volumen', color='orange')
    plt.xlabel('Fecha')
    plt.ylabel('Volume')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig3)
     
    
if st.checkbox('Tether'):
    st.markdown('Tether es una criptomoneda estable vinculada al dólar estadounidense. Se utiliza como refugio de valor en momentos de volatilidad y facilita el comercio en exchanges al proporcionar estabilidad de precio.')
    fig1= plt.figure(figsize=(10, 6))
    plt.plot(teter['FECHAS'], teter['PRECIO-usd'], label='Precio de Cierre', color='blue')
    plt.xlabel('Fecha')
    plt.ylabel('Precio USD')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig1)
    
    
    fig2= plt.figure(figsize=(10, 6))
    plt.plot(teter['FECHAS'], teter['MARKET_CAP-usd'], label='market cap', color='red')
    plt.xlabel('Fecha')
    plt.ylabel('Market Cap')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig2)
    
    
    fig3= plt.figure(figsize=(10, 6))
    plt.plot(teter['FECHAS'], teter['TOTAL_VOLUMES'], label='volumen', color='orange')
    plt.xlabel('Fecha')
    plt.ylabel('Volume')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig3)
     
        
if st.checkbox('Binance Coin'):
    st.markdown('BNB es la moneda nativa de la plataforma de intercambio Binance. Se utiliza para pagar tarifas de transacción en la plataforma y ha ganado popularidad debido a su utilidad y a las ventas de tokens en la plataforma.')
    fig1= plt.figure(figsize=(10, 6))
    plt.plot(bnb['FECHAS'], bnb['PRECIO-usd'], label='Precio de Cierre', color='blue')
    plt.xlabel('Fecha')
    plt.ylabel('Precio USD')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig1)
    
    
    fig2= plt.figure(figsize=(10, 6))
    plt.plot(bnb['FECHAS'], bnb['MARKET_CAP-usd'], label='market cap', color='red')
    plt.xlabel('Fecha')
    plt.ylabel('Market Cap')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig2)
    
    
    fig3= plt.figure(figsize=(10, 6))
    plt.plot(bnb['FECHAS'], bnb['TOTAL_VOLUMES'], label='volumen', color='orange')
    plt.xlabel('Fecha')
    plt.ylabel('Volume')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig3)
     
    
if st.checkbox('XRP'):
    st.markdown('Ripple se enfoca en facilitar transferencias internacionales de dinero de manera rápida y eficiente. Aunque ha enfrentado desafíos regulatorios, su enfoque en soluciones de pagos globales sigue siendo relevante en la industria.')
    fig1= plt.figure(figsize=(10, 6))
    plt.plot(xrp['FECHAS'], xrp['PRECIO-usd'], label='Precio de Cierre', color='blue')
    plt.xlabel('Fecha')
    plt.ylabel('Precio USD')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig1)
    
    
    fig2= plt.figure(figsize=(10, 6))
    plt.plot(xrp['FECHAS'], xrp['MARKET_CAP-usd'], label='market cap', color='red')
    plt.xlabel('Fecha')
    plt.ylabel('Market Cap')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig2)
    
    
    fig3= plt.figure(figsize=(10, 6))
    plt.plot(xrp['FECHAS'], xrp['TOTAL_VOLUMES'], label='volumen', color='orange')
    plt.xlabel('Fecha')
    plt.ylabel('Volume')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig3)
     
    
if st.checkbox('USD Coin'):
    st.markdown('Similar a Tether, USDC es una criptomoneda estable vinculada al dólar estadounidense. Ofrece estabilidad de valor y es ampliamente utilizado en exchanges y aplicaciones financieras.')
    fig1= plt.figure(figsize=(10, 6))
    plt.plot(usd['FECHAS'], usd['PRECIO-usd'], label='Precio de Cierre', color='blue')
    plt.xlabel('Fecha')
    plt.ylabel('Precio USD')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig1)
    
    
    fig2= plt.figure(figsize=(10, 6))
    plt.plot(usd['FECHAS'], usd['MARKET_CAP-usd'], label='market cap', color='red')
    plt.xlabel('Fecha')
    plt.ylabel('Market Cap')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig2)
    
    
    fig3= plt.figure(figsize=(10, 6))
    plt.plot(usd['FECHAS'], usd['TOTAL_VOLUMES'], label='volumen', color='orange')
    plt.xlabel('Fecha')
    plt.ylabel('Volume')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig3)
     
    
if st.checkbox('Lido Staker Ether'):
    st.markdown('STETH es una forma de participar en Ethereum 2.0, una actualización de Ethereum para mejorar su escalabilidad y eficiencia. Los poseedores de STETH obtienen recompensas por validar transacciones en la red Ethereum.')
    fig1= plt.figure(figsize=(10, 6))
    plt.plot(lido['FECHAS'], lido['PRECIO-usd'], label='Precio de Cierre', color='blue')
    plt.xlabel('Fecha')
    plt.ylabel('Precio USD')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig1)
    
    
    fig2= plt.figure(figsize=(10, 6))
    plt.plot(lido['FECHAS'], lido['MARKET_CAP-usd'], label='market cap', color='red')
    plt.xlabel('Fecha')
    plt.ylabel('Market Cap')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig2)
    
    
    fig3= plt.figure(figsize=(10, 6))
    plt.plot(lido['FECHAS'], lido['TOTAL_VOLUMES'], label='volumen', color='orange')
    plt.xlabel('Fecha')
    plt.ylabel('Volume')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig3)
     
    
if st.checkbox('Cardano'):
    st.markdown('Cardano se centra en la investigación científica y el desarrollo de soluciones blockchain escalables y sostenibles. Ofrece un enfoque único en la gobernanza y la investigación académica.')
    fig1= plt.figure(figsize=(10, 6))
    plt.plot(car['FECHAS'], car['PRECIO-usd'], label='Precio de Cierre', color='blue')
    plt.xlabel('Fecha')
    plt.ylabel('Precio USD')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig1)
    
    
    fig2= plt.figure(figsize=(10, 6))
    plt.plot(car['FECHAS'], car['MARKET_CAP-usd'], label='market cap', color='red')
    plt.xlabel('Fecha')
    plt.ylabel('Market Cap')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig2)
    
    
    fig3= plt.figure(figsize=(10, 6))
    plt.plot(car['FECHAS'], car['TOTAL_VOLUMES'], label='volumen', color='orange')
    plt.xlabel('Fecha')
    plt.ylabel('Volume')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig3)
     

if st.checkbox('Solana'):
    st.markdown('Solana destaca por su alta velocidad y escalabilidad, lo que lo hace adecuado para aplicaciones descentralizadas de alto rendimiento y DeFi.')
    fig1= plt.figure(figsize=(10, 6))
    plt.plot(sol['FECHAS'], sol['PRECIO-usd'], label='Precio de Cierre', color='blue')
    plt.xlabel('Fecha')
    plt.ylabel('Precio USD')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig1)
    
    
    fig2= plt.figure(figsize=(10, 6))
    plt.plot(sol['FECHAS'], sol['MARKET_CAP-usd'], label='market cap', color='red')
    plt.xlabel('Fecha')
    plt.ylabel('Market Cap')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig2)
    
    
    fig3= plt.figure(figsize=(10, 6))
    plt.plot(sol['FECHAS'], sol['TOTAL_VOLUMES'], label='volumen', color='orange')
    plt.xlabel('Fecha')
    plt.ylabel('Volume')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig3)
     
    
if st.checkbox('Doge Coin'):
    st.markdown('Dogecoin comenzó como una broma, pero ha ganado una comunidad activa. Aunque tiene un enfoque menos serio, ha ganado popularidad y atención en los medios.')
    fig1= plt.figure(figsize=(10, 6))
    plt.plot(doge['FECHAS'], doge['PRECIO-usd'], label='Precio de Cierre', color='blue')
    plt.xlabel('Fecha')
    plt.ylabel('Precio USD')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig1)
    
    
    fig2= plt.figure(figsize=(10, 6))
    plt.plot(doge['FECHAS'], doge['MARKET_CAP-usd'], label='market cap', color='red')
    plt.xlabel('Fecha')
    plt.ylabel('Market Cap')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig2)
    
    
    fig3= plt.figure(figsize=(10, 6))
    plt.plot(doge['FECHAS'], doge['TOTAL_VOLUMES'], label='volumen', color='orange')
    plt.xlabel('Fecha')
    plt.ylabel('Volume')
    plt.legend()
    plt.grid(True)
    st.plotly_chart(fig3)
     