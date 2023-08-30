import streamlit as st

#logo_path = '/Users/flori/Desktop/DATA SCIENCE/LABS/Trabajos/tp2/DASHBOARD_TP2/png-transparent-cryptocurrency-exchange-trade-bitcoin-foreign-exchange-market-bitcoin-trademark-service-logo.png'  
logo_path= 'png-transparent-cryptocurrency-exchange-trade-bitcoin-foreign-exchange-market-bitcoin-trademark-service-logo.png'
st.image(logo_path, width=500)

st.title('🪙Introduciéndonos al mundo de las criptomonedas🪙')

st.markdown('*****')
st.markdown('### 💲¡Ya es hora! En esta APP vas a poder comenzar tu investigación sobre el mundo de los activos digitales.💲 ')


if st.checkbox('**¿Qué son las criptomonedas?**'):
    st.write('Una criptomoneda es un activo digital que emplea un cifrado criptográfico para  garantizar su titularidad y asegurar la integridad de las transacciones, y controlar la creación de unidades adicionales. Son monedas digitales que operan gracias a una red mundial de pagos usuario a usuario, descentralizada, no necesita de bancos ni instituciones financieras')

if st.checkbox('**¿Cuántas criptomonedas hay?**'):
    st.write('CoinMarketCap ha aportado datos que señalan que actualmente existen 22.932 criptomonedas. Pero no te preocupes, nuestra idea es hablar solo de algunas, para que no sea tan complicado.')
    
if st.checkbox('**¿Cómo funciona el sistema de transacciones o intercambio de criptomonedas?**'):
    st.write('Las criptomonedas funcionan mediante el registro contable compartido o blockchain. Esta tecnología les aporta un elevado sistema de seguridad con capacidad para evitar, por ejemplo, que un mismo activo digital se pueda transferir en dos ocasiones o que sea falsificado.')
    
if st.checkbox('**¿Qué es un sistema blockchain?**'):
    st.write('Blockchain se puede definir como una estructura matemática para almacenar datos de una manera que es casi imposible de falsificar. Es un libro electrónico público que se puede compartir abiertamente entre usuarios dispares y que crea un registro inmutable de sus transacciones.')


if st.checkbox('**¿Dónde se guardan las criptomonedas?¿Cómo puedo adquirirlas?**'):
    st.write('Las wallets son la forma de almacenar tus criptomonedas, ya sea virtuales, de escritorio o fisicas(hardware). Estos monederos son dispositivos físicos que se usan para almacenar nuestras claves privadas de forma segura. Para adquirir criptomonedas de forma segura y simple, lo más recomendable es que utilices alguna de las diversas plataformas y páginas en línea que operan con bitcoins y otras criptomonedas, conocidas popularmente como exchanges.')


if st.checkbox('**¿Qué quiere decir que sea un sistema descentralizado?**'):
    st.write('No hay un organismo central que regule la emisión de dinero nuevo. Las reglas para generar el dinero están fijadas en el protocolo lanzado en 2009. Desde entonces, el protocolo elimina la necesidad de un ente regulador, como un Gobierno o una institución. El dinero pasa directamente a manos de los usuarios, en forma de mineros, sin que haya una institución que medie en la puesta en circulación. En el caso del sistema fiduciario, serían entidades como el Banco Central Europeo y el Banco de España.')    

st.markdown('*****')
st.write('👨🏻‍🔬👩🏻‍🔬**Si queres mas información te dejamos algunos links que pueden ser de utilidad**')
if st.button('MAS INFO'):
    st.write('[Binance](https://academy.binance.com/en)')
    st.write('[CMC](https://coinmarketcap.com/alexandria)')
    st.write('[Coingecko](https://www.coingecko.com/en/api)')