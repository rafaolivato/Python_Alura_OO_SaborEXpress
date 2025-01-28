class ItemCardapio:
    # Inicializando o atributo de classe `itens_cardapio` como uma lista vazia
    itens_cardapio = []

    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        self._status = True
        self._avaliacao = []
        # Adiciona a instância atual à lista de itens do cardápio
        ItemCardapio.itens_cardapio.append(self)

    def __str__(self):
        return f"{self._nome} - R${self._preco:.2f}"

