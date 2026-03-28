import psycopg2
from src.modelagem import df_pacientes, df_setores, df_atendimentos  # ou ajuste o import

def conexao():
    conn = psycopg2.connect(
    host="localhost",
    database="hospital",
    user="postgres",
    password="Ap200112.",
    port="5433"
    )
    return conn

print("conectado com sucesso")

cursor = conexao().cursor()

# Tabela pacientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS pacientes (
    id_paciente INT PRIMARY KEY,
    paciente_nome TEXT
);
""")

# Tabela setores
cursor.execute("""
CREATE TABLE IF NOT EXISTS setores (
    id_setor INT PRIMARY KEY,
    setor TEXT
);
""")

# Tabela atendimentos
cursor.execute("""
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
""")

conexao().commit()

print("Tabelas criadas com sucesso!")


for _, row in df_pacientes.iterrows():
    cursor.execute("""
        INSERT INTO pacientes (id_paciente, paciente_nome)
        VALUES (%s, %s)
        ON CONFLICT (id_paciente) DO NOTHING
    """, (row['id_paciente'], row['paciente_nome']))

conexao().commit()

for _, row in df_setores.iterrows():
    cursor.execute("""
        INSERT INTO setores (id_setor, setor)
        VALUES (%s, %s)
        ON CONFLICT (id_setor) DO NOTHING
    """, (row['id_setor'], row['setor']))

conexao().commit()

for _, row in df_atendimentos.iterrows():
    cursor.execute("""
        INSERT INTO atendimentos (
            id_atendimento,
            id_paciente,
            id_setor,
            tempo_espera_min,
            data_atendimento,
            eh_outlier
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (id_atendimento) DO NOTHING
    """, (
        row['id_atendimento'],
        row['id_paciente'],
        row['id_setor'],
        row['tempo_espera_min'],
        row['data_atendimento'],
        row['eh_outlier']
    ))

conexao().commit()

print("Dados de pacientes, setores e atendimentos inseridos!")

cursor.close()
conexao().close()