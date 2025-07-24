from app.database.db_config import get_connection

class ClienteModel:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def criar_cliente(self, nome, email):
        sql = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
        self.cursor.execute(sql, (nome, email))
        self.conn.commit()

    def listar_clientes(self):
        self.cursor.execute("SELECT * FROM clientes")
        return self.cursor.fetchall()
