class Avaliacao:
    def __init__(self,cliente, nota):
        self._cliente = cliente
        self._nota = nota
        

    def to_dict(self):
        return {
            
            'nome': self.nome,
            'nota': self.nota,
            
        }