import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv("data/data.csv")
    return df

df = load_data()

st.title(" Análise de Preços")

#FILTROS
st.sidebar.header("Filtros - Análise de Preços")

marcas_disponiveis = sorted(df["Make"].dropna().unique().tolist())
marca_selecionada = st.sidebar.multiselect(
    "Marcas:",
    options=marcas_disponiveis,
    default=marcas_disponiveis[:8]
)

anos_min = int(df["Year"].min())
anos_max = int(df["Year"].max())
intervalo_anos = st.sidebar.slider(
    "Intervalo de anos:",
    min_value=anos_min,
    max_value=anos_max,
    value=(anos_min, anos_max)
)

tipos_transmissao = sorted(df["Transmission Type"].dropna().unique().tolist())
transmissao_sel = st.sidebar.multiselect(
    "Tipo de transmissão:",
    options=tipos_transmissao,
    default=tipos_transmissao
)

df_filtrado = df.copy()

if marca_selecionada:
    df_filtrado = df_filtrado[df_filtrado["Make"].isin(marca_selecionada)]

df_filtrado = df_filtrado[
    (df_filtrado["Year"] >= intervalo_anos[0]) &
    (df_filtrado["Year"] <= intervalo_anos[1])
]

if transmissao_sel:
    df_filtrado = df_filtrado[df_filtrado["Transmission Type"].isin(transmissao_sel)]

st.write(f"Dados filtrados: **{df_filtrado.shape[0]}** registros.")

#LAYOUT EM TABS
tab1, tab2 = st.tabs(["Scatter de Preços", "Boxplot por Marca"])

#GRÁFICO 3
with tab1:
    st.subheader("Preço em função do ano ou da potência (HP)")

    eixo_x_opcao = st.radio(
        "Selecione o eixo X:",
        options=["Year", "Engine HP"],
        format_func=lambda x: "Ano" if x == "Year" else "Potência (Engine HP)",
        horizontal=True
    )

    fig_scatter = px.scatter(
        df_filtrado,
        x=eixo_x_opcao,
        y="MSRP",
        color="Make",
        hover_data=["Model", "Year", "Engine HP"],
        labels={"MSRP": "Preço (MSRP)"},
        title=f"Preço vs {eixo_x_opcao}"
    )
    fig_scatter.update_traces(opacity=0.7)
    st.plotly_chart(fig_scatter, use_container_width=True)

#GRÁFICO 4
with tab2:
    st.subheader("Distribuição de preço por marca (Boxplot)")

    marcas_top = (
        df_filtrado.groupby("Make")["MSRP"]
        .median()
        .sort_values(ascending=False)
        .head(10)
        .index
        .tolist()
    )

    df_box = df_filtrado[df_filtrado["Make"].isin(marcas_top)]

    fig_box = px.box(
        df_box,
        x="Make",
        y="MSRP",
        labels={"Make": "Marca", "MSRP": "Preço (MSRP)"},
        title="Distribuição de preço por marca (Top 10)"
    )
    fig_box.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_box, use_container_width=True)