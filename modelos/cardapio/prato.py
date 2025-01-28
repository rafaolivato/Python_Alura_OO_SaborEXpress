from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)  # Inicializa os atributos da classe base ItemCardapio
        self._descricao = descricao  # Adiciona o atributo exclusivo de Prato

    def __str__(self):
        return f"{self._nome} - {self._descricao} - R${self._preco:.2f}"
