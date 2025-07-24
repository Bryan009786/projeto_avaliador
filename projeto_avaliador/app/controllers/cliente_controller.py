from app.models.cliente_model import ClienteModel

class ClienteController:
    def __init__(self):
        # Instância do model responsável pelas operações no banco de dados
        self.model = ClienteModel()

    def adicionar_cliente(self, nome: str, email: str) -> bool:
        """
        Adiciona um cliente ao banco de dados.
        Retorna True se sucesso, False em caso de erro.
        """
        try:
            self.model.criar_cliente(nome, email)
            return True
        except Exception as e:
            # Aqui pode ser um log, print ou tratamento específico
            print(f"Erro ao adicionar cliente: {e}")
            return False

    def obter_clientes(self) -> list:
        """
        Retorna uma lista de clientes cadastrados.
        """
        try:
            clientes = self.model.listar_clientes()
            return clientes
        except Exception as e:
            print(f"Erro ao obter clientes: {e}")
            return []

    def editar_cliente(self, cliente_id: int, nome: str, email: str) -> bool:
        """
        Atualiza os dados de um cliente existente.
        """
        try:
            self.model.atualizar_cliente(cliente_id, nome, email)
            return True
        except Exception as e:
            print(f"Erro ao editar cliente: {e}")
            return False

    def deletar_cliente(self, cliente_id: int) -> bool:
        """
        Remove um cliente do banco pelo ID.
        """
        try:
            self.model.excluir_cliente(cliente_id)
            return True
        except Exception as e:
            print(f"Erro ao deletar cliente: {e}")
            return False
