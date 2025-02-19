import random
from streamlit_gsheets import GSheetsConnection 
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

url = "https://docs.google.com/spreadsheets/d/1Fzn_rBCR1aelDaS4E4ClSHyttdLF5jiZR8AO6QGx7C4/edit#gid=0"
conn = st.connection("gsheets", type=GSheetsConnection)
        

if 'jogadores' not in st.session_state:
    st.session_state.jogadores = ""

if 'lista' not in st.session_state:
    st.session_state.lista = ["Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador"]
    
if 'contador' not in st.session_state:
    st.session_state.contador = 0

if "time1" not in st.session_state:
    st.session_state["time1"] = []

if 'time2' not in st.session_state:
    st.session_state.time2 = []

if 'time3' not in st.session_state:
    st.session_state.time3 = []

if 'time4' not in st.session_state:
    st.session_state.time4 = []

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
                box-shadow: rgba(127,255,0, 0.35) 0px 5px 15px;
                border: 1px solid rgba(127,255,0);
                }
                
            .card { 
                    border: 1px solid rgba(127,255,0);
                    border-radius: 10px; 
                    background-color: rgba(31,76,44);
                    color: white;
                    text-align: center;
                    align-items:center;
                    padding: 10px; 
                    margin: 5px;
                    }
            .card-1 { 
                    border: 1px solid rgba(127,255,0);
                    border-radius: 10px; 
                    background-color: rgba(183,215,186);
                    color: rgba(31,76,44);
                    text-align: center;
                    align-items:center;
                    padding: 10px; 
                    margin: 5px;
                    }
            .card2{
                border: 1px solid rgba(127,255,0);
                    border-radius: 10px; 
                    background-color: rgba(218,214,8);
                    color: white;
                    text-align: center;
                    align-items:center;
                    padding: 10px; 
                    margin: 5px;
            }
            .card-2 { 
                    border: 1px solid rgba(127,255,0);
                    border-radius: 10px; 
                    background-color: rgba(254, 255, 178);
                    color: rgba(31,76,44);
                    text-align: center;
                    align-items:center;
                    padding: 10px; 
                    margin: 5px;
                    }
            
            .card3 {
                    border: 1px solid rgba(1, 255, 247);
                    border-radius: 10px; 
                    background-color: rgba(0, 29, 189);
                    color: white;
                    text-align: center;
                    align-items:center;
                    padding: 10px; 
                    margin: 5px;
            }
            .card-3 { 
                    border: 1px solid rgba(3, 253, 215);
                    border-radius: 10px; 
                    background-color: rgba(127, 187, 240);
                    color: rgba(31,76,44);
                    text-align: center;
                    align-items:center;
                    padding: 10px; 
                    margin: 5px;
                    }
            
            .card4{
                    border: 1px solid rgba(247,61,163);
                    border-radius: 10px; 
                    background-color: rgba(238, 3, 253);
                    color: white;
                    text-align: center;
                    align-items:center;
                    padding: 10px; 
                    margin: 5px;
            }
            .card-4 { 
                    border: 1px solid rgba(127,255,0);
                    border-radius: 10px; 
                    background-color: rgba(252, 199, 255);
                    color: rgba(31,76,44);
                    text-align: center;
                    align-items:center;
                    padding: 10px; 
                    margin: 5px;
                    }
            
            .grid-container {
                text-align: center;
            }
            ''', unsafe_allow_html=True)


st.markdown("<h1 class='titulo'>ORGANIZADOR DE TIMES</h1>", unsafe_allow_html=True)

with st.form("Adicionar jogador"):
    jogador = st.text_input("Adicione o jogador", value="")
    adicionar = st.form_submit_button("Adicionar")
    tamanho = len(jogador.strip())
    if (adicionar == True) and (jogador.strip() != "") and (tamanho > 1) and (st.session_state.contador < 16):
        print(jogador)
        if st.session_state.jogadores == "":
            st.session_state.jogadores = jogador
        else:
            st.session_state.jogadores = st.session_state.jogadores + f";{jogador}"
            st.success(f"Jogador {jogador} Adicionado!")
            print(st.session_state.jogadores)
    else:
        st.warning("Insira um nome de jogador")

dados = st.session_state.jogadores.split(";")
df= pd.DataFrame(dados, columns=["nome"])



if adicionar:
    lista = ["Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador","Sem jogador"]
    st.session_state.lista = lista
    i=0

    for row in df.itertuples(index=True): 
        lista[i] = row.nome
        st.session_state.lista = lista
        i += 1
        st.session_state.contador = i
    
    print(f"Estado: {st.session_state.lista}")
    print(f"Contador: {st.session_state.contador}")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write(f'''
                <div class="grid-container">
                    <div class="card"><strong>Time 1</strong></div>
                    <div class="card-1"><strong>1 - {st.session_state.lista[0]}</strong></div>
                    <div class="card-1"><strong>2 - {st.session_state.lista[1]}</strong></div>
                    <div class="card-1"><strong>3 - {st.session_state.lista[2]}</strong></div>
                    <div class="card-1"><strong>4 - {st.session_state.lista[3]}</strong></div>
                </div>
            ''',unsafe_allow_html=True)
with col2:
    st.write(f'''
                <div class="grid-container">
                    <div class="card2"><strong>Time 2</strong></div>
                    <div class="card-2"><strong>5 - {st.session_state.lista[4]}</strong></div>
                    <div class="card-2"><strong>6 - {st.session_state.lista[5]}</strong></div>
                    <div class="card-2"><strong>7 - {st.session_state.lista[6]}</strong></div>
                    <div class="card-2"><strong>8 - {st.session_state.lista[7]}</strong></div>
                </div>
            ''',unsafe_allow_html=True)
with col3:
    st.write(f'''
                <div class="grid-container">
                    <div class="card3"><strong>Time 3</strong></div>
                    <div class="card-3"><strong>9 - {st.session_state.lista[8]}</strong></div>
                    <div class="card-3"><strong>10 - {st.session_state.lista[9]}</strong></div>
                    <div class="card-3"><strong>11 - {st.session_state.lista[10]}</strong></div>
                    <div class="card-3"><strong>12 - {st.session_state.lista[11]}</strong></div>
                </div>
            ''',unsafe_allow_html=True)
with col4:
    st.write(f'''
                <div class="grid-container">
                    <div class="card4"><strong>Time 4</strong></div>
                    <div class="card-4"><strong>13 - {st.session_state.lista[12]}</strong></div>
                    <div class="card-4"><strong>14 - {st.session_state.lista[13]}</strong></div>
                    <div class="card-4"><strong>15 - {st.session_state.lista[14]}</strong></div>
                    <div class="card-4"><strong>16 - {st.session_state.lista[15]}</strong></div>
                </div>
            ''',unsafe_allow_html=True)
with st.container():
    col5, col6 = st.columns(2)
    
    with col5:        
        misturar = st.button("Misturar")
        if misturar:
            print(f"antes: {st.session_state.lista}")
            
            random.shuffle(st.session_state.lista)
            print(f"Misturado: {st.session_state.lista}")
            st.rerun()
    with col6:
        salvar = st.button("Salvar")
        if salvar:
            n = 1
            i = 0
            for jogador in st.session_state.lista:
                st.session_state[f"time{n}"].append(jogador)
                
                if (i == 3) or (i == 7) or (i == 11):
                     n += 1
                i += 1
            
            print(st.session_state.time1)
            print(st.session_state.time2)
            print(st.session_state.time3)
            print(st.session_state.time4)
            
            dados = {
                        "Time 1":[st.session_state.time1],
                        "Time 2": [st.session_state.time2], 
                        "Time 3": [st.session_state.time3],
                        "Time 4": [st.session_state.time4]
                    }
            
            new_data = pd.DataFrame(dados, columns=['Time 1','Time 2','Time 3','Time 4'])
                
            st.success("Times salvos com sucesso!")
            new_data
            #Atualizando a planilha
            conn.update(spreadsheet=url, data=new_data)
            #st.rerun()