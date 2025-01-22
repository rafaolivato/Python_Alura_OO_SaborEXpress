class Restaurante:
    restaurantes = []

    def __init__(self,nome,categoria): # Método construtor (__init__) com dois parâmetros (self e nome)
        self.nome = nome
        self.categoria = categoria
        self.status = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self): # Método Especial que retorna uma string
        return f'{self.nome}' | f'{self.categoria}'
       
    @staticmethod
    def listar_restaurantes(): # Criando meu próprio método
        for r in Restaurante.restaurantes:
            print(f'Nome: {r.nome} | Categoria: {r.categoria} | Status: {r.status}')

restaurante_praca = Restaurante('Restaurante da Praça','Prato Feito') 
restaurante_pizza = Restaurante('Pizzaria do Paulista','Pizzaria')

Restaurante.listar_restaurantes()

