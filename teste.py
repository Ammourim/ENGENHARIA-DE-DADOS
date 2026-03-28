from sqlalchemy import text
from src.database.connection import get_engine

engine = get_engine()

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    
    for row in result:
        print(row)

print("Conectado com sucesso!")