import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


@st.cache # Armazena os arquivos na memória cache
def load_data(file_path): # Usado para carregar o arquivo de dados
    data = pd.read_csv(file_path) # Lê o arquivo CSV
    return data # Retorna os dados

file_path = "C:/Users/thiag/OneDrive/Documents/estudosPython/data/IMDBdata.csv"
movies_data = load_data(file_path) # Usa load_data para carregar o arquivo CSV e armazena os dados em movies_data

st.title("Análise de dados de filmes")

st.header("Visualização de dados") 
if st.checkbox("Mostrar dados"): 
    st.write(movies_data.head()) # Mostra as primeiras linhas de dados de filmes quando a caixa é marcada

st.subheader("Distribuição de gêneros") 
if "genre" in movies_data.columns: # verifica se a coluna genre está no conjunto de dados.
    genre_counts = movies_data["genre"].value_counts().head(10) # conta os 10 gêneros mais comuns
    st.bar_chart(genre_counts) # Cria um gráfico de barras 

st.subheader("Correlação: Avaliação x Classificação ")
if "imdbRating" in movies_data.columns and "imdbVotes" in movies_data.columns: 
    fig, ax = plt.subplots() # Cria uma área para o gráfico usando o matplotlib
    sns.scatterplot(data=movies_data, x="imdbRating", y="imdbVotes", ax=ax) # Cria um gráfico de  
    st.pyplot(fig) # Exibe o gráfico

st.header("Estimativa de avaliação")

# Seleção de dados para o modelo
ml_data = movies_data[["imdbRating", "imdbVotes", "metacritic"]].dropna() # Filtra as colunas necessárias (imdbRating, imdbVotes, metacritic)
X = ml_data[["imdbRating", "imdbVotes"]] 
y = ml_data["metacritic"] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # 80% pra ensinar e 20% para avaliar o desempenho

model = LinearRegression() # Regressão linear
model.fit(X_train, y_train) # Treina o modelo usando X e y

y_pred = model.predict(X_test) # Faz previsões com os dados de teste
mse = mean_squared_error(y_test, y_pred) # Calcula o erro quadrático médio entre as previsões

st.subheader("Resultados")
st.write("Erro quadrático médio:", mse) 

st.subheader("________________________________")
rating = st.number_input("classificação IMDB", min_value=0.0, max_value=10.0, step=0.1) 
votes = st.number_input("Número de avaliações no IMDb", min_value=0, step=100)

if st.button("Prever contagem"):
    pred = model.predict([[rating, votes]]) # Faz uma previsão baseada nos números inseridos pelo usuário
    st.write(f"Contagem estimada: {pred[0]:.2f}") 