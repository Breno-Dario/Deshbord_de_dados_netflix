import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
# Define o título da página, o ícone e o layout para ocupar a largura
#inteira.
st.set_page_config(
    page_title="Dashboard da Netflix",
    page_icon="📊",
    layout="wide",    #deixa página formato largo
)

# --- Carregamento dos dados ---
df =pd.read_csv("https://raw.githubusercontent.com/profzappa/profGit/refs/heads/master/netflix_titles.csv")

st.sidebar.header("🔍 Filtros")

# Filtro de Ano
# Filter for movies

anos_disponiveis = sorted(df['release_year'].unique())
anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis,
default=anos_disponiveis)

# Filtro de tipos (Filme ou séries)
tipos_disponiveis = sorted(df['type'].unique())
tipos_selecionados = st.sidebar.multiselect("Tipos", tipos_disponiveis,
default=tipos_disponiveis)

# --- Filtragem do DataFrame ---
# O dataframe principal é filtrado com base nas seleções feitas na barra
#lateral.
##criou componente visual dos filtros, agora, aplicar os filtros, pegando
#tudo o que o usuário selecionou

df_filtrado = df[
    (df['release_year'].isin(anos_selecionados)) &
    (df['type'].isin(tipos_selecionados)) 
]

# --- Conteúdo Principal ---
st.title("🎲 Dashboard de Filmes/Séries Netflix")
st.markdown("Explore os dados de Filmes e Séries na área de dados nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.")

# --- Métricas Principais (KPIs) ---
st.subheader("Métricas gerais (Filmes / Séries)")

if not df_filtrado.empty:
    
    total_registros = df_filtrado.shape[0]
    tipo_mais_frequente = df_filtrado["type"].mode()[0]
else:
    total_registros, tipo_mais_frequente = 0, 0

col1, col2 = st.columns(2)

col1.metric("Total de registros", f"{total_registros:,}")
col2.metric("Tipo mais frequente", tipo_mais_frequente)

st.markdown("---")

# --- Análises Visuais com Plotly --- 
st.subheader("Gráficos")  ##subtitulos

col_graf1, col_graf2 = st.columns(2)   ##2 colunas, um do lado do outro

with col_graf1:
    if not df_filtrado.empty:
        top_paises = df['country'].value_counts().head(10).reset_index()
        top_paises.columns = ['país', 'quantidade']
        grafico_paises = px.bar(
            top_paises,
            x='país',
            y='quantidade',
            orientation='v',
            title="Top 10 Países com mais Produções na Netflix",
            labels={'país': 'Países', 'quantidade': 'qtde'}
        )
        grafico_paises.update_layout(title_x=0.1,
yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.")

with col_graf2:
    if not df_filtrado.empty:
        filmes_por_ano =df_filtrado['release_year'].value_counts().reset_index()
        filmes_por_ano.columns = ['release_year', 'quantidade']
        grafico_filmes = px.pie(
            filmes_por_ano,
            values='quantidade',
            names='release_year',
            title="Proporção de Filmes/Séries por Ano de Lançamento"
            )
        grafico_filmes.update_layout(title_x=0.1)
        st.plotly_chart(grafico_filmes, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de proporção de filmes.")

# --- Tabela de Dados Detalhados ---
st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)
