import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor

st.title("🏙️ Projeto Assistido: Boston")
st.subheader("Desenvolvido por Karolynne - ADS IFPE")

try:
    data = pd.read_csv("data.csv")
    st.write("Dados carregados com sucesso!")
    
    # Treinando o modelo (Slide 64)
    x = data.drop("MEDV", axis=1)
    y = data["MEDV"]
    
    rf_regressor = RandomForestRegressor()
    rf_regressor.fit(x, y)
    
    st.write("### Tabela de Dados (Primeiras Linhas)")
    st.dataframe(data.head())
    
    st.write("### Gráfico de Análise")
    fig = px.scatter(data, x="RM", y="MEDV", title="Número de Quartos vs Preço")
    st.plotly_chart(fig)

except:
    st.error("Ainda não achei o arquivo data.csv no seu GitHub! Suba ele lá para os dados aparecerem.")
