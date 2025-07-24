import mysql.connector
import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Erro na conexão com o banco de dados: {err}")
        return None
