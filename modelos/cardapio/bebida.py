from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    bebidas =[]
    
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho
        Bebida.bebidas.append(self)
    
    def __str__(self):
        return f'{self.nome} - R$ {self.preco:.2f}\nTamanho: {self.tamanho}'
    
    @property
    def tamanho(self):
        return self._tamanho
    
    @classmethod
    def listar_bebidas(cls):
        print(f"{'Nome da Bebida'.ljust(20)} | {'Preço'.ljust(12)} | {'Tamanho'.ljust(20)}")
        print("-" * 47)
        for bebida in cls.bebidas:
            print(f"{bebida.nome.ljust(20)} | {str(bebida.preco).ljust(12)} | {bebida.tamanho.ljust(20)}")
            
    def aplicar_desconto(self):
        self._preco *= 0.95
        self._preco = round(self._preco, 2)
        return self._preco