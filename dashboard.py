import streamlit as st
import psycopg2
from src.database.connection import get_engine
import pandas as pd
import plotly.express as px


# -------------------------
# CONFIG
# -------------------------
st.set_page_config(page_title="Dashboard Hospitalar", layout="wide")

# ---------------------
# QUERY
# ---------------------
@st.cache_data
def carregar_dados():
    engine = get_engine()
    query = """
        SELECT
            a.id_atendimento,
            p.paciente_nome,
            s.setor,
            a.tempo_espera_min,
            a.data_atendimento,
            a.eh_outlier
        FROM atendimentos a
            JOIN pacientes p ON a.id_paciente = p.id_paciente
            JOIN setores s ON a.id_setor = s.id_setor
        """
    df = pd.read_sql(query, engine)
    return df

# -------------------------
# APP
# -------------------------

st.title("Relatório Estratégico de Performance de Atendimentos")

df = carregar_dados()

df_limpo = df[df["eh_outlier"] == False] 
df_limpo.pop("eh_outlier")

#FILTROS 
st.sidebar.header("Filtros")

setores = df_limpo["setor"].unique()

setor_selecionado = st.sidebar.selectbox(
    "Selecione o setor",
    ["Todos"] + list(setores)
)

if setor_selecionado != "Todos":
    df_limpo = df_limpo[df_limpo["setor"] == setor_selecionado]

st.subheader("Dados de atendimentos")
st.dataframe(df_limpo)

#tempo medio geral sem outliers

col1, col2, col3 = st.columns(3)

tempo_medio = df_limpo["tempo_espera_min"].mean()
total_atendimentos = len(df_limpo)
total_pacientes = df_limpo["paciente_nome"].nunique()
col1.metric("Tempo médio de espera (min)", round(tempo_medio, 2))
col2.metric("Total de atendimentos", round(total_atendimentos, 2))
col3.metric("Total de pacientes únicos", round(total_pacientes, 2))

#tempo medio por setor
media_setor = (
    df_limpo
    .groupby("setor")["tempo_espera_min"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
    .round(2)
)
#grafico media por setor

st.subheader("Tempo médio por setor")
st.bar_chart(data=media_setor,
             x="setor",
             y="tempo_espera_min")

media_setor.index += 1 #ajustando para o indice começar em 1
st.subheader("Tempo medio por setor")
st.dataframe(media_setor)



st.subheader("Distribuição do Tempo de Espera")

# Criando um histograma para ver a frequência dos tempos
histograma = px.histogram(
    df_limpo, 
    x="tempo_espera_min",
    title=None,
    labels={'tempo_espera_min': 'Tempo de Espera (min)'}
)

# Remove o excesso de margens e deixa o visual limpo
histograma.update_yaxes(title_text="Frequência (Nº de Pacientes)")
histograma.update_layout(margin=dict(l=20, r=20, t=20, b=20))

st.plotly_chart(histograma, use_container_width=True)
