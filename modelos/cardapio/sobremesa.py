from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    sobremesas = []
    
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self._tipo = (tipo.capitalize())
        self._tamanho = (tamanho.title())
        self._descricao = (descricao.capitalize())
        Sobremesa.sobremesas.append(self)
        
    @property
    def tipo(self):
        return self._tipo
    @property
    def tamanho(self):
        return self._tamanho
    @property
    def descricao(self):
        return self._descricao
    
    def __str__(self):
        return f'{self.nome} - R$ {self.preco:.2f}\nTipo: {self.tipo}\nTamanho: {self.tamanho}\nDescrição: {self.descricao}'
    
    def aplicar_desconto(self):
        pass
    
    
    
    
    
    
    