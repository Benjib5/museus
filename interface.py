import streamlit as st

st.title('Title')

st.image("https://assets.masp.org.br/uploads/temp/WEB_IM_MASP_10834_01.jpg", width=50)
if st.button('Click me'):
   st.write('Button clicked!')

with st.sidebar:
   st.header('Salut')
   st.write('Seu aplicativo de dicas de saúde!')
   st.caption('Criado por ...')
