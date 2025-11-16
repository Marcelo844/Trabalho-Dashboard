# 🚗 Dashboard de Carros — Análise Exploratória com Streamlit

Este projeto apresenta um **dashboard interativo** desenvolvido com **Streamlit**, utilizando dados do Kaggle sobre características de veículos e seus respectivos preços (MSRP).  
O objetivo é permitir a exploração visual do dataset, ajudando a identificar padrões, tendências e relações importantes.

---

## 📊 Funcionalidades do Dashboard

O dashboard está dividido em **múltiplas páginas**, cada uma focada em uma análise específica:

### **1. Página Principal**
- Explicação do objetivo do dashboard  
- Descrição de como navegar entre as seções  
- Descrição de como os filtros influenciam os gráficos  
- Prévia do dataset e suas colunas  

### **2. Visão Geral**
- Filtros por marca e intervalo de anos  
- Métricas principais (preço médio, ano médio, popularidade média)  
- Gráfico de **Preço Médio por Marca (Top 10)**  
- **Histograma de Preços**  

### **3. Análise de Preços**
- Filtros avançados (marca, ano, tipo de transmissão)  
- Scatter interativo relacionando **Preço × Ano** ou **Preço × Potência (HP)**  
- Boxplot comparando preços entre as marcas  

### **4. Consumo e Performance**
- Filtros por tamanho do veículo e tipo de tração  
- Gráfico interativo relacionando **Consumo na Cidade × Estrada**  
- Gráfico de **Popularidade Média por Tamanho do Veículo**

---

## 📁 Estrutura do Projeto

Trabalho_Dashboard/
│── app.py
│── requirements.txt
│── data/
│ └── data.csv
└── pages/
├── 1_Visao_Geral.py
├── 2_Analise_de_Precos.py
└── 3_Consumo_e_Performance.py


---

## 🧪 Dataset Utilizado

**Car Features and MSRP**  
Disponível no Kaggle:  
https://www.kaggle.com/datasets/CooperUnion/cardataset

Tamanho: **11.914 linhas e 16 colunas**  
Contém informações como:
- Marca e modelo  
- Ano  
- Potência (HP)  
- Tipo de transmissão  
- Consumo (cidade e estrada)  
- Tamanho do veículo  
- Tipo de tração  
- Popularidade  
- Preço sugerido (MSRP)  

---

## 🚀 Como executar o projeto localmente

### **1. Instale as dependências**
No terminal:
pip install -r requirements.txt


### **2. Execute o Streamlit*`*
python -m streamlit run app.py

O dashboard abrirá automaticamente no navegador em:
http://localhost:8501

☁️ Deploy na Nuvem (Streamlit Cloud)
https://principalpy-uys4bxoymd9mi4cff3s6ma.streamlit.app/

🛠 Tecnologias Utilizadas

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)

Streamlit

Pandas

Plotly
