import streamlit as st

st.set_page_config(layout="wide")

st.markdown('''
            <style>
            
            .stMarkdown{
                margin-bottom: 50px;
            }
            
            .titulo{
                border-radius: 20px;
                text-align: center;
                box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
            }
            
            .e1obcldf2{
                background-color: yellow;
                color: green;
                font-weight: bold;
            }
            
            .e1obcldf2:hover{
                background-color: green;
                color: yellow;    
            }
            
            .red{
                border-radius: 20px;
                background-color: red;
                text-align: center;
                color: white;
                font-weight: bold;
                font-size: 150px;
            }
            
            .blue{
                border-radius: 20px;
                background-color: blue;
                text-align: center;
                font-weight: bold;
                color: white;
                font-size: 150px;
            }
            
            
            </style>''',unsafe_allow_html=True)


if not "placar1" in st.session_state:
    st.session_state.placar1 = 0

if not "placar2" in st.session_state:
    st.session_state.placar2 = 0

if not "mais" in st.session_state:
    st.session_state.mais = 0

if not "menos" in st.session_state:
    st.session_state.menos = 0



st.markdown("<h1 class='titulo'>PLACAR</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    col3, col4 = st.columns(2)
    
    with col3:
        mais = st.button("Acrescentar", use_container_width=True)    
    with col4:
        menos = st.button("Retirar", use_container_width=True, type="secondary")
        
    if mais == True:
        st.session_state.placar1 += 1
        print(f"{st.session_state.placar1}")
    if menos == True:
        st.session_state.placar1 -= 1
        print(f"{st.session_state.placar1}")
    
    st.markdown(f"<div class='red'>{st.session_state.placar1}</div>",unsafe_allow_html=True)
    
with col2:
    col5, col6 = st.columns(2)
    
    with col5:
        mais = st.button(" Acrescentar", use_container_width=True)    
    with col6:
        menos = st.button(" Retirar", use_container_width=True, type="secondary")
        
    if mais == True:
        st.session_state.placar2 += 1
        print(f"{st.session_state.placar2}")
    if menos == True:
        st.session_state.placar2 -= 1
        print(f"{st.session_state.placar2}")
    
    st.markdown(f"<div class='blue'>{st.session_state.placar2}</div>",unsafe_allow_html=True)