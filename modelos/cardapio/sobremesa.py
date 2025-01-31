from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo):
        # Passando nome, preco e tipo para o construtor da classe base (ItemCardapio)
        super().__init__(nome, preco)
        self._tipo = tipo  # Atributo exclusivo de sobremesa

    def __str__(self):
        return f"{self._nome} ({self._tipo})  R${self._preco:.2f}"

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.04)  # Exemplo de desconto
