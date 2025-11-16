import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard de Carros",
    page_icon="🚗",
    layout="wide"
)

@st.cache_data
def load_data():
    # Lê o dataset a partir da pasta data/
    df = pd.read_csv("data/data.csv")
    return df

df = load_data()

st.title("🚗 Dashboard de Carros")

st.markdown("""
### 🎯 Objetivo do Dashboard

Este dashboard tem como objetivo **explorar um conjunto de dados de carros**,
permitindo analisar:

- Distribuição de preços (MSRP);
- Diferenças entre marcas e anos;
- Consumo de combustível na cidade e na estrada;
- Características técnicas (potência, cilindros, tamanho do veículo, etc.);
- Popularidade dos veículos.

---

### 🧭 Como navegar entre as seções

Use o menu no canto superior esquerdo do Streamlit (ícone ☰) para acessar as páginas:

- **Visão Geral** – visão macro do dataset, métricas e gráficos iniciais;
- **Análise de Preços** – foco em preço por marca, ano, transmissão;
- **Consumo & Performance** – análise de consumo (cidade/estrada) e desempenho.

Cada página possui **filtros na barra lateral** (sidebar), que atualizam os gráficos em tempo real.

---

### 🎚️ Como os filtros influenciam os dados

- Filtros como **marca, ano, tipo de transmissão, tamanho do veículo e tipo de tração**
  são aplicados diretamente sobre o conjunto de dados.
- Todos os gráficos daquela página são atualizados com base no subconjunto filtrado.
- Assim, é possível identificar **padrões e relações**, como:
  - Marcas com maior preço médio;
  - Relação entre consumo e tamanho do carro;
  - Diferença de preço por tipo de transmissão.

---

### 📂 Prévia do Dataset
Abaixo você pode ver algumas linhas do dataset para entender a estrutura dos dados.
""")

st.dataframe(df.head())

st.markdown(
    f"**Número de linhas:** {df.shape[0]} &nbsp;&nbsp;|&nbsp;&nbsp; "
    f"**Número de colunas:** {df.shape[1]}"
)

st.markdown("""
**Principais colunas do dataset:**

- `Make` – Marca do carro  
- `Model` – Modelo  
- `Year` – Ano  
- `Engine Fuel Type` – Tipo de combustível  
- `Engine HP` – Potência (HP)  
- `Engine Cylinders` – Número de cilindros  
- `Transmission Type` – Tipo de transmissão  
- `Driven_Wheels` – Tipo de tração  
- `Number of Doors` – Número de portas  
- `Market Category` – Categoria de mercado  
- `Vehicle Size` – Tamanho do veículo  
- `Vehicle Style` – Estilo do veículo  
- `highway MPG` – Consumo na estrada (milhas por galão)  
- `city mpg` – Consumo na cidade (milhas por galão)  
- `Popularity` – Popularidade  
- `MSRP` – Preço sugerido (em dólares)
""")
