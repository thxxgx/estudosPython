**Documentação do Projeto: Análise de Filmes**

**O que é o projeto?**

Esse projeto é uma aplicação interativa feita com **Streamlit**, que analisa dados de filmes e até faz predições com machine learning. A ideia é explorar informações de um dataset do IMDb, mostrar gráficos legais e usar um modelo para prever uma métrica de qualidade dos filmes.![ref1]

**O que você precisa instalar?**

Antes de começar, instale essas bibliotecas.

**Streamlit**: Cria a interface web da aplicação. É com ela que você vai ver os gráficos e interagir.

pip install streamlit

●

**Pandas**: Trabalha com os dados, como carregar o arquivo e organizar as colunas.

pip install pandas

●

**Seaborn**: Faz gráficos bonitos, como o scatter plot que usamos.

pip install seaborn

●

**Matplotlib**: Dá suporte gráfico e ajuda o Seaborn a funcionar melhor.

pip install matplotlib

●

**scikit-learn**: Faz toda a mágica de machine learning: divide os dados, treina o modelo e calcula as métricas.

pip install scikit-learn

●![ref1]

**Como funciona o projeto?**

1. **Carregar e visualizar os dados**
- O arquivo CSV com os dados do IMDb é carregado com **Pandas**, e usamos o @st.cache\_data do Streamlit pra melhorar a performance.
- Você pode visualizar as primeiras linhas do dataset marcando uma caixinha na interface.
- A aplicação também mostra:
- Um gráfico de barras com os gêneros de filmes mais populares.
- Um scatter plot que mostra a relação entre a nota no IMDb (*imdbRating*) e o número de votos (*imdbVotes*).
2. **Treinar o modelo de Machine Learning**
- Pegamos algumas colunas específicas (*imdbRating*, *imdbVotes* e *metacritic*) para fazer as análises.
- Dividimos os dados em treino e teste usando o **scikit-learn**.
- Criamos um modelo de regressão linear simples pra prever a nota *Metacritic*.
- Avaliamos o modelo calculando o Erro Médio Quadrático (MSE), que mostra o quanto o modelo erra.
3. **Predições personalizadas**
- Você pode inserir valores de *IMDb Rating* e *Número de Votos* na interface.
- O modelo usa esses números pra prever a nota *Metacritic* e te dá um resultado.![ref1]

**Como rodar o projeto?**

**streamlit run app.py**

[ref1]: Aspose.Words.4f9dee89-2105-443f-be65-cd81482d897d.001.png
