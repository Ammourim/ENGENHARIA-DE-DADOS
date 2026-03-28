#%%
import streamlit as st
import psycopg2
from src.database import conexao
import pandas as pd
#%%
# -------------------------
# CONFIG
# -------------------------
st.set_page_config(page_title="Dashboard Hospitalar", layout="wide")
#%%

# ---------------------
# QUERY
# ---------------------
def carregar_dados():
    conn = conexao()
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
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# -------------------------
# APP
# -------------------------
st.title("Dashboard Hospitalar")

df = carregar_dados()
#%%
df_limpo = df[df["eh_outlier"] == False] 
df_limpo.pop("eh_outlier")
df_limpo
#%%
st.subheader("Dados de atendimentos")
st.dataframe(df_limpo)

#tempo medio geral sem outliers
#%%

col1, col2, col3 = st.columns(3)

tempo_medio = df_limpo["tempo_espera_min"].mean()
total_atendimentos = len(df_limpo)
total_pacientes = df["paciente_nome"].nunique()
col1.metric("Tempo médio de espera (min)", round(tempo_medio, 2))
col2.metric("Total de atendimentos", round(total_atendimentos, 2))
col3.metric("Total de pacientes únicos", round(total_pacientes, 2))
# %%
#tempo medio por setor
media_setor = (
    df_limpo
    .groupby("setor")["tempo_espera_min"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
    .round(2)
)

media_setor.index += 1 #ajustando para o indice começar em 1
st.subheader("Tempo medio por setor")
st.dataframe(media_setor)
# %%
st.subheader("Distribuição do Tempo de Espera")
st.line_chart(df_limpo["tempo_espera_min"])

st.sidebar.header("Filtros")

setores = df_limpo["setor"].unique()

setor_selecionado = st.sidebar.selectbox(
    "Selecione o setor",
    ["Todos"] + list(setores)
)

if setor_selecionado != "Todos":
    df_limpo = df_limpo[df_limpo["setor"] == setor_selecionado]
