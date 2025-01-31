from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('Restaurante da Praça', 'Prato Feito')

sobremesa_sorvete = Sobremesa('Sorvete', 10.0, 'Gelato Italiano')
sobremesa_sorvete.aplicar_desconto()
sobremesa_pudim = Sobremesa('Pudim', 15.0, 'Doce Popular')
sobremesa_pudim.aplicar_desconto()
bebida_suco = Bebida('Suco de Laranja', 5.0, '300ml')
bebida_suco.aplicar_desconto()
prato_feijoada = Prato('Feijoada', 20.0, 'Feijoada completa com arroz, farofa e couve')
prato_feijoada.aplicar_desconto()
restaurante_praca.adicionar_cardapio(bebida_suco)
restaurante_praca.adicionar_cardapio(prato_feijoada)
restaurante_praca.adicionar_cardapio(sobremesa_pudim)
restaurante_praca.adicionar_cardapio(sobremesa_sorvete)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
