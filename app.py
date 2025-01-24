
from modelos.restaurante import Restaurante 

restaurante_praca = Restaurante('Restaurante da Praça','Prato Feito')



restaurante_praca.receber_avaliacao('João',5)
restaurante_praca.receber_avaliacao('Maria',4)
restaurante_praca.receber_avaliacao('José',3)

restaurante_praca.alternar_status()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()