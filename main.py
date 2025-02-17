import streamlit as st

st.set_page_config(layout="wide")

st.markdown('''
            <style>
            *{
                padding: 0;
                margin: 0;
            }
            
            .stMarkdown{
                margin-bottom: 50px;
            }
            
            .titulo{
                border-radius: 20px;
                text-align: center;
                box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
            }
            
            .e1obcldf2{
                border-radius: 20px;
                background-color: blue;
                text-align: center;
                color: white;
                font-weight: bold;
                margin: 0;
                padding: 0;
            }
            
            .e1obcldf2 p{
                font-size: 200px;
                margin: 0;
            }
            
            .e1obcldf2:hover{
                color: white;
                background-color: blue;
            }
            
            .e1obcldf3{
                border-radius: 20px;
                background-color: red;
                text-align: center;
                color: white;
                font-weight: bold;
                font-size: 200px;
                margin: 0;
                padding: 0;
            }
            
            .e1obcldf3 p{
                font-size: 200px;
                margin: 0;
            }
            
            .e1obcldf3:hover{
                color: white;
            }
            
            .red{
                border-radius: 20px;
                background-color: red;
                text-align: center;
                color: white;
                font-weight: bold;
                font-size: 200px;
                margin: 0;
                padding: 0;
            }
            
            .blue{
                border-radius: 20px;
                background-color: blue;
                text-align: center;
                font-weight: bold;
                color: white;
                font-size: 200px;
                margin: 0;
                padding: 0;
            }
            
            
            </style>''',unsafe_allow_html=True)


if not "placar1" in st.session_state:
    st.session_state.placar1 = 0

if not "placar2" in st.session_state:
    st.session_state.placar2 = 0

if not "ponto1" in st.session_state:
    st.session_state.ponto1 = False

if not "ponto2" in st.session_state:
    st.session_state.ponto2 = False

def placar(index):
    if index != 0:
        st.session_state[f"placar{index}"] += 1
        print(f"{st.session_state[f"placar{index}"]}")

def retirar(index):
    if index != 0:
        st.session_state[f"placar{index}"] -= 1
        print(f"{st.session_state[f"placar{index}"]}")

st.markdown("<h1 class='titulo'>PLACAR</h1>", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    ponto1 = st.button(f"{st.session_state.placar1}", use_container_width=True, type="secondary")
    
    if ponto1:
        placar(1)
        st.rerun()
        
with col2:
    ponto2 = st.button(f"{st.session_state.placar2}", use_container_width=True, type="tertiary")
    if ponto2:
        placar(2)
        st.rerun()

with st.expander("Retirar ponto"):
    with st.form("Retirar ponto"):
        time = st.radio("Escolha o time para reirar pontos",
                        ["Time 1","Time 2"],
                        index=None
                        )
        
        escolha = st.form_submit_button("Retirar")
        if escolha:
            if time == "Time 1":
                st.session_state.placar1 -= 1
                st.rerun()
            elif time == "Time 2":
                st.session_state.placar2 -= 1
                st.rerun()