import mysql.connector
import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env (que deve estar no mesmo diretório)
load_dotenv()

def get_connection():
    try:
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        database = os.getenv("DB_NAME")

        # DEBUG: imprimir variáveis para verificar (remova depois)
        print(f"Conectando a: host={host}, user={user}, database={database}")

        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Conexão bem sucedida!")
        return conn

    except mysql.connector.Error as err:
        print(f"Erro na conexão com o banco de dados: {err}")
        return None

if __name__ == "__main__":
    get_connection()
