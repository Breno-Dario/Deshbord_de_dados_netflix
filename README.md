# 🎬 Dashboard Netflix com Streamlit

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

## 📌 Sobre o Projeto

Este projeto é um **dashboard interativo** desenvolvido com **Streamlit**, que permite explorar dados de filmes e séries da Netflix de forma dinâmica e visual.


## 🚀 Funcionalidades

- 🔍 Filtros interativos:
  - Ano de lançamento
  - Tipo (Filme ou Série)
- 📊 Métricas principais (KPIs):
  - Total de registros
  - Tipo mais frequente
- 📈 Visualizações com Plotly:
  - Top 10 países com mais produções
  - Distribuição por ano de lançamento
- 📋 Tabela com dados filtrados em tempo real


## 🛠️ Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Plotly Express

## 📂 Fonte dos Dados

Dataset público:
```bash
https://raw.githubusercontent.com/profzappa/profGit/refs/heads/master/netflix_titles.csv
``` 
## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

## 2. Instale as dependências
```bash
pip install streamlit pandas plotly
```

## 3. Execute o projeto
```bash
streamlit run app.py
```
## 📊 Estrutura do Dashboard
- 🔍 Filtros (Sidebar)
  - Seleção de anos
  - Seleção de tipo (Movie / TV Show)
- 📊 Métricas
  - Total de registros
  - Tipo mais frequente
- 📊 Gráficos
   - Bar Chart: Top países com mais produções
   - Pie Chart: Distribuição por ano
- 📊 Tabela
Dados detalhados com base nos filtros aplicados
