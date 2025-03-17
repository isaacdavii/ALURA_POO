from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    def __str__(self):
        return f'{self.nome} - R$ {self.preco:.2f}'
    
    @property
    def nome(self):
        return self._nome
    @property
    def preco(self):
        return self._preco
    
    @abstractmethod # Método abstrato que obriga a implementação nas classes filhas
    def aplicar_desconto(self):
        pass 
    
    