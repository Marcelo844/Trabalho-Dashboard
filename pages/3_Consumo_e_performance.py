import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv("data/data.csv")
    return df

df = load_data()

st.title("⚙️ Consumo e Performance")

#FILTROS
st.sidebar.header("Filtros - Consumo & Performance")

tamanhos = sorted(df["Vehicle Size"].dropna().unique().tolist())
tam_sel = st.sidebar.multiselect(
    "Tamanho do veículo:",
    options=tamanhos,
    default=tamanhos
)

tipos_tracao = sorted(df["Driven_Wheels"].dropna().unique().tolist())
tracao_sel = st.sidebar.multiselect(
    "Tipo de tração (Driven Wheels):",
    options=tipos_tracao,
    default=tipos_tracao
)

df_filtrado = df.copy()

if tam_sel:
    df_filtrado = df_filtrado[df_filtrado["Vehicle Size"].isin(tam_sel)]

if tracao_sel:
    df_filtrado = df_filtrado[df_filtrado["Driven_Wheels"].isin(tracao_sel)]

st.write(f"Dados filtrados: **{df_filtrado.shape[0]}** registros.")

#LAYOUT EM COLUNAS
col1, col2 = st.columns(2)

#GRÁFICO 5
with col1:
    st.subheader("Consumo: cidade x estrada")

    fig_consumo = px.scatter(
        df_filtrado,
        x="city mpg",
        y="highway MPG",
        color="Vehicle Size",
        hover_data=["Make", "Model", "Year"],
        labels={
            "city mpg": "Consumo na cidade (city mpg)",
            "highway MPG": "Consumo na estrada (highway MPG)"
        },
        title="Relação entre consumo na cidade e na estrada"
    )
    fig_consumo.update_traces(opacity=0.7)
    st.plotly_chart(fig_consumo, use_container_width=True)

#GRÁFICO 6
with col2:
    st.subheader("Popularidade média por tamanho do veículo")

    pop_por_tam = (
        df_filtrado.groupby("Vehicle Size")["Popularity"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig_pop = px.bar(
        pop_por_tam,
        x="Vehicle Size",
        y="Popularity",
        labels={"Vehicle Size": "Tamanho do veículo", "Popularity": "Popularidade média"},
        title="Popularidade média por tamanho do veículo"
    )
    st.plotly_chart(fig_pop, use_container_width=True)