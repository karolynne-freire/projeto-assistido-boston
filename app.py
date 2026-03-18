import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Projeto Boston - Karolynne", layout="wide")

st.title("🏙️ Projeto Assistido: Boston")
st.subheader("Análise de Dados e Predição - ADS IFPE")

try:
    data = pd.read_csv("data.csv")
    st.success("✅ Arquivo 'data.csv' carregado com sucesso!")

    df_modelo = data.drop(columns=['CATEGORIAS'], errors='ignore')
    
    x = df_modelo.drop("MEDV", axis=1)
    y = df_modelo["MEDV"]

    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_regressor.fit(x, y)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.write("### 📊 Visualização da Tabela")
        st.write("Abaixo estão as 10 primeiras linhas do seu dataset:")
        st.dataframe(data.head(10))

    with col2:
        st.write("### 📈 Gráfico de Dispersão")
        fig = px.scatter(
            data, 
            x="RM", 
            y="MEDV", 
            color="CATEGORIAS", 
            title="Relação: Número de Quartos (RM) vs Preço (MEDV)",
            labels={"RM": "Nº de Quartos", "MEDV": "Preço Médio (mil $)"}
        )
        st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.info("💡 Dica: No Streamlit Cloud, qualquer alteração que você fizer no GitHub atualizará este site automaticamente.")

except Exception as e:
    st.error(f"❌ Erro ao carregar os dados ou treinar o modelo: {e}")
    st.warning("Verifique se o arquivo 'data.csv' está na mesma pasta que o 'app.py' no seu GitHub.")
