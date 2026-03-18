# 🧠🏡 Projeto Assistido Boston  
### Predição de Valores de Imóveis com Inteligência Artificial

🔗 **Acesse a aplicação:**  
https://projeto-assistido-boston-karolynne.streamlit.app/

---

## 📚 Sobre o Projeto

Este projeto foi desenvolvido como parte da disciplina de **Inteligência Artificial**, com o objetivo de aplicar conceitos de **Machine Learning** na predição de valores de imóveis.

A aplicação utiliza um dataset clássico de Boston e permite ao usuário interagir com os dados e visualizar resultados de forma dinâmica.

---

## 🚀 Funcionalidades

- Interface interativa com **Streamlit**
- Entrada de dados pelo usuário (sidebar)
- Visualização de dataset
- Treinamento de modelo em tempo real
- Predição de valor de imóveis
- Feedback visual com métricas e animações 🎈

---

## 🧠 Tecnologias Utilizadas

- Python  
- Streamlit  
- Pandas  
- Scikit-learn (Random Forest)  

---

## ⚙️ Como Funciona

1. O sistema carrega o dataset (`data.csv`)  
2. O usuário define características do imóvel  
3. O modelo de Machine Learning é treinado  
4. A aplicação retorna um valor estimado  

---

## 📥 Entradas do Usuário

- Taxa de criminalidade (**CRIM**)  
- Proporção de áreas comerciais (**INDUS**)  
- Proximidade com o rio (**CHAS**)  
- Concentração de óxido nítrico (**NOX**)  
- Número de quartos (**RM**)  
- Relação aluno/professor (**PTRATIO**)  

---

## 📈 Resultado

Ao clicar em **"Realizar predição"**, o sistema exibe:

- 💰 Valor estimado do imóvel  
- 🎉 Feedback visual interativo  

---

## 📊 Análise Exploratória de Dados

A análise exploratória dos dados será incorporada em versões futuras do projeto, incluindo gráficos e insights sobre as variáveis utilizadas na predição dos valores dos imóveis.

---

## ⚙️ Como Executar Localmente

```bash
# Clone o repositório
git clone https://github.com/karolynne-freire/projeto-assistido-boston.git

# Entre na pasta
cd projeto-assistido-boston

# Instale as dependências
pip install -r requirements.txt

# Execute o projeto
streamlit run app.py
```
---

## ⭐ Considerações Finais

Este projeto representa a aplicação prática de conceitos de IA, unindo análise de dados, modelagem preditiva e interface interativa, proporcionando uma experiência acessível ao usuário.
