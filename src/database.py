import psycopg2

conn = psycopg2.connect(
    host="172.31.80.1",
    database="hospital",
    user="postgres",
    password="Ap200112.",
    port="5433"
)

print("conectado com sucesso")

cursor = conn.cursor()

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

conn.commit()

print("Tabelas criadas com sucesso!")

cursor.close()
conn.close()