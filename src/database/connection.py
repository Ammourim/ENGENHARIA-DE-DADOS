from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    usuario = os.getenv("DB_USER")
    senha = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    porta = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")

    url = f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{db}"

    engine = create_engine(url)

    return engine