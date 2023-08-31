import streamlit as st

#logo_path = ''  
#st.image(logo_path, width=250)

st.title('Algunas conclusiones finales')

st.markdown('*****')
st.markdown('### Uno de los acrónimos clásicos en la cultura cripto es DYOR, o lo que es lo mismo, Do-Your-Own-Research. Investiga sobre la moneda, en los canales oficiales, los foros, los perfiles sociales… Investiga, analiza y decide. ')
st.write('****')

if st.button('VENTAJAS'):
    st.write('✔️SISTEMA DESCENTRALIZADO')
    st.write('✔️DEFLACIONARIO')
    st.write('✔️MAS PRIVACIDAD')
    st.write('✔️EN CONSTANTE CRECIMIENTO')
    
if st.button('DESVENTAJAS'):
    st.write('❌VOLATILIDAD')
    st.write('❌COMPLEJO')