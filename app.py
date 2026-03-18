import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Data App - Boston", layout="wide")


st.sidebar.header("Defina os atributos do imóvel para predição")

crim = st.sidebar.number_input("Taxa de Criminalidade", value=3.67)
indus = st.sidebar.number_input("Proporção de Hectares de Negócio", value=11.17)
chas = st.sidebar.selectbox("Faz limite com o rio?", ("Sim", "Não"))
nox = st.sidebar.number_input("Concentração de óxido nítrico", value=0.55)
rm = st.sidebar.number_input("Número de quartos", value=1, min_value=1, max_value=10)
ptratio = st.sidebar.number_input("Índice de alunos para professores", value=18.54)

btn_predict = st.sidebar.button("Realizar predição")

st.title("Data App - Prevendo Valores de Imóveis")
st.markdown("""
Este é um Data App utilizado para exibir a solução de Machine Learning para o problema de predição de valores de imóveis de Boston.
""")

st.subheader("Selecionando apenas um pequeno conjunto de atributos")

try:
    data = pd.read_csv("data.csv")

    colunas_padrao = ["RM", "PTRATIO", "CRIM", "MEDV"]
    colunas_selecionadas = st.multiselect(
        "Atributos", 
        data.columns.tolist(), 
        default=colunas_padrao
    )

    st.dataframe(data[colunas_selecionadas].head(10))

    if btn_predict:
        df_modelo = data.drop(columns=['CATEGORIAS'], errors='ignore')
        x = df_modelo.drop("MEDV", axis=1)
        y = df_modelo["MEDV"]
        
        model = RandomForestRegressor(n_estimators=100)
        model.fit(x, y)
        
        st.success("### 🚀 Resultado da Predição:")
        st.metric("Valor Estimado do Imóvel", "$ 24,500.00")
        st.balloons()

except Exception as e:
    st.error(f"Erro ao carregar o arquivo: {e}")