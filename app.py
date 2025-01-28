from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('Restaurante da Praça', 'Prato Feito')

bebida_suco = Bebida('Suco de Laranja', 5.0, '300ml')
prato_feijoada = Prato('Feijoada', 20.0, 'Feijoada completa com arroz, farofa e couve')

restaurante_praca.adicionar_cardapio(bebida_suco)
restaurante_praca.adicionar_cardapio(prato_feijoada)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
