#%%
import streamlit as st
import psycopg2
from src.database import conexao
import pandas as pd
#%%
st.title("Dashboard Hospitalar")

st.write("Meu primeiro dashboard de engenharia de dados!")

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

df = carregar_dados()

st.subheader("Dados de atendimentos")
st.dataframe(df)

#tempo medio geral sem outliers
#%%
df_filtrado = df[df["eh_outlier"] == False]

tempo_medio = df_filtrado["tempo_espera_min"].mean()
st.metric("Tempo médio de espera (min)", round(tempo_medio, 2))
# %%
#tempo medio por setor

media_setor = (
    df_filtrado
    .groupby("setor")["tempo_espera_min"]
    .mean()
    .reset_index()
)

st.subheader("Tempo medio por setor")
st.dataframe(media_setor)