import streamlit as st
import principal
import dachboard
#cores
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

#login
st.title('Seja bem vindo á VendaGest')
st.write('## Faça o login')

usuario = st.text_input('Digite seu nome: ')
senha = st.text_input('Digite sua senha: ', type='password')

if senha in ['1234', '4321', 'pedro']:
    st.button('Entrar')
    st.switch_page('pages/principal.py')
    st.success('Ok, click no botão acima para avançar.')

else:
    st.error('Tente novamente.')  

st.write('## Sobre a VendaGest')     
st.write('-> A VendaGest é um site para você ter controle da sua empresa ou seu negocio.')
st.write('Na VendaGest você tem acesso a graficos e tabelas de finaças da sua empresa.')

st.write('Para ter mais informações acesse nosso instagram ou entre em contato com nossos desenvolvedores.')

