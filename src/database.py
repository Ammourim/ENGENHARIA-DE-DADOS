from sqlalchemy import text
from src.database.connection import get_engine
from src.modelagem import df_pacientes, df_setores, df_atendimentos

engine = get_engine()

print("Conectado com sucesso!")

# -------------------------
# CRIAR TABELAS
# -------------------------
with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id_paciente INT PRIMARY KEY,
            paciente_nome TEXT
        );
    """))

    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS setores (
            id_setor INT PRIMARY KEY,
            setor TEXT
        );
    """))

    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS atendimentos (
            id_atendimento INT PRIMARY KEY,
            id_paciente INT,
            id_setor INT,
            tempo_espera_min FLOAT,
            data_atendimento TIMESTAMP,
            eh_outlier BOOLEAN,
            FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
            FOREIGN KEY (id_setor) REFERENCES setores(id_setor)
        );
    """))

print("Tabelas criadas com sucesso!")

# -------------------------
# INSERIR DADOS
# -------------------------
print("Inserindo dados nas tabelas...")

df_pacientes.to_sql('pacientes', con=engine, if_exists='append', index=False)
df_setores.to_sql('setores', con=engine, if_exists='append', index=False)
df_atendimentos.to_sql('atendimentos', con=engine, if_exists='append', index=False)

print("Dados inseridos com sucesso!")