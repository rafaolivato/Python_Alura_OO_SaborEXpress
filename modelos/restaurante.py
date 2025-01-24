from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):  # Método construtor (__init__) com dois parâmetros (self e nome)
        self._nome = nome.title()  # Atributo público --> self.nome
        self.categoria = categoria.upper()
        self._status = False  # Atributo protegido (privado) --> _status
        self._avaliacao = []  # Atributo protegido (privado) --> _avaliacao
        Restaurante.restaurantes.append(self)

    def __str__(self):  # Método Especial que retorna uma string
        return f'{self._nome} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):  # Criando meu próprio método
        print(f'{"Nome do Restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Avaliação".ljust(20)} | {"Status"}')
        for r in cls.restaurantes:
            # Convertendo a média da avaliação para string e aplicando ljust para alinhamento
            print(f'{r._nome.ljust(20)} | {r.categoria.ljust(20)} | {str(r.media_avaliacao).ljust(20)} | {r.status}')

    @property
    def status(self):
        return "❎" if self._status else "❌"

    def alternar_status(self):
        self._status = not self._status

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <=5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '--'  # Retorna -- se não houver avaliações
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)
        return media

# Exemplo de uso
# Restaurante.listar_restaurantes()  # Isto pode ser chamado depois de adicionar restaurantes à lista
