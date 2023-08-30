import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('ROI')

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

bitcoin['FECHAS']=pd.to_datetime(bitcoin['FECHAS']).dt.date
bnb['FECHAS']=pd.to_datetime(bnb['FECHAS']).dt.date
car['FECHAS']=pd.to_datetime(car['FECHAS']).dt.date
doge['FECHAS']=pd.to_datetime(doge['FECHAS']).dt.date
eter['FECHAS']=pd.to_datetime(eter['FECHAS']).dt.date
lido['FECHAS']=pd.to_datetime(lido['FECHAS']).dt.date
sol['FECHAS']=pd.to_datetime(sol['FECHAS']).dt.date
teter['FECHAS']=pd.to_datetime(teter['FECHAS']).dt.date
usd['FECHAS']=pd.to_datetime(usd['FECHAS']).dt.date
xrp['FECHAS']=pd.to_datetime(xrp['FECHAS']).dt.date

df_crypto_dashboard = pd.concat([bitcoin, bnb,car,doge,eter,lido,sol,teter,usd,xrp], axis=0)

st.subheader('🔷 Selecciona un token')
selected_token = st.selectbox('Elije un token:', df_crypto_dashboard['COIN_ID'].unique())

df_selected_token = df_crypto_dashboard[df_crypto_dashboard['COIN_ID'] == selected_token]

st.header('Ganancias y Pérdidas 💰')
st.write("¿ón (ROI).")

selected_investment_date = st.date_input('Selecciona una fecha para invertir:')
selected_future_date = st.date_input('Selecciona una fecha futura:')
investment_amount = st.number_input('Inversión en USD:', min_value=0.0)

if selected_investment_date and selected_future_date and investment_amount > 0:
    investment_row = df_selected_token[df_selected_token['FECHAS'] == selected_investment_date]
    future_row = df_selected_token[df_selected_token['FECHAS'] == selected_future_date]
    
    if not investment_row.empty and not future_row.empty:
        initial_price = investment_row['PRECIO-usd'].values[0]
        future_price = future_row['PRECIO-usd'].values[0]
        
        potential_gain = investment_amount * (future_price / initial_price)
        roi = ((future_price - initial_price) / initial_price) * 100
        
        st.write(f" Si hubieras invertido ${investment_amount:.2f} dolares en  {selected_token}  el  {selected_investment_date}, "
                 f" a la fecha  {selected_future_date}  podrias haber obtenido un valor de  {potential_gain:.2f}  dolares en {selected_token}.")
        
        # Mostrar ROI
        st.markdown(f'Retorno de Inversion (Return on Investment "ROI"): **{roi:.2f}%**', unsafe_allow_html=True)

        fig_change = px.bar(
            x=['Valor Inicial', 'Valor Futuro'],
            y=[initial_price, future_price],
            title='Cambio en el Valor',
            labels={'x': 'Valor', 'y': 'Precio'}
        )
        fig_change.update_traces(marker_color=['#3498db', '#2ecc71'])
        fig_change.update_traces(marker_line_width=0, marker_line_color='white')
        st.plotly_chart(fig_change)
        
    else:
        st.warning('Alguna de las fechas seleccionadas no está en el conjunto de datos o el token no coincide.')
