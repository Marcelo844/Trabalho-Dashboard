import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv("data/data.csv")
    return df

df = load_data()

st.title(" Visão Geral dos Dados de Carros")

#FILTROS
st.sidebar.header("Filtros - Visão Geral")

marcas_disponiveis = sorted(df["Make"].dropna().unique().tolist())
marca_selecionada = st.sidebar.multiselect(
    "Selecione uma ou mais marcas:",
    options=marcas_disponiveis,
    default=marcas_disponiveis[:5]  # primeiras 5 marcas como padrão
)

anos_min = int(df["Year"].min())
anos_max = int(df["Year"].max())
intervalo_anos = st.sidebar.slider(
    "Selecione o intervalo de anos:",
    min_value=anos_min,
    max_value=anos_max,
    value=(anos_min, anos_max)
)

df_filtrado = df.copy()

if marca_selecionada:
    df_filtrado = df_filtrado[df_filtrado["Make"].isin(marca_selecionada)]

df_filtrado = df_filtrado[
    (df_filtrado["Year"] >= intervalo_anos[0]) &
    (df_filtrado["Year"] <= intervalo_anos[1])
]

st.write(f"Dados filtrados: **{df_filtrado.shape[0]}** registros.")

#MÉTRICAS
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Preço médio (MSRP)", f"${df_filtrado['MSRP'].mean():,.2f}")
with col2:
    st.metric("Ano médio", f"{df_filtrado['Year'].mean():.0f}")
with col3:
    st.metric("Popularidade média", f"{df_filtrado['Popularity'].mean():.0f}")

st.markdown("---")

#GRÁFICO 1
st.subheader("Preço médio por marca (Top 10)")

preco_medio_marca = (
    df_filtrado.groupby("Make")["MSRP"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_bar = px.bar(
    preco_medio_marca,
    x="Make",
    y="MSRP",
    labels={"Make": "Marca", "MSRP": "Preço médio (MSRP)"},
    title="Top 10 marcas por preço médio"
)
fig_bar.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_bar, use_container_width=True)

#GRÁFICO 2
st.subheader("Distribuição de preços (MSRP)")

fig_hist = px.histogram(
    df_filtrado,
    x="MSRP",
    nbins=40,
    labels={"MSRP": "Preço (MSRP)"},
    title="Histograma de preços"
)
st.plotly_chart(fig_hist, use_container_width=True)