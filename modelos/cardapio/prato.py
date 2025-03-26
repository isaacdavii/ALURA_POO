from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):  # Prato is a subclass of ItemCardapio
    """
    Essa classe vai herda métodos e atributos de uma outra classe (ItemCardapio)
     e adicionar um novo atributo (descricao).
    A herança é um conceito fundamental na programação orientada a objetos (OO)
     e desempenha um papel crucial no desenvolvimento de software.
     A importância da herança está relacionada à capacidade de criar novas classes
     reutilizando ou estendendo o comportamento de classes existentes.
    """
    pratos = []
    
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)  # Chama o construtor da classe pai.
        # Permite que acesse informações de outra classe. Nesse caso, nome e preço
        # super() é uma função que retorna o objeto pai da classe atual
        self._descricao = (descricao.capitalize())
        Prato.pratos.append(self)

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}\n{self.descricao}"

    @property
    def descricao(self):
        return self._descricao
    
    @classmethod
    def listar_pratos(cls):
        print(f"{'Nome do Prato'.ljust(20)} | {'Preço'.ljust(12)} | {'Descrição'}")
        print("-" * 55)
        for prato in cls.pratos:
            print(f"{prato.nome.ljust(20)} | {str(prato.preco).ljust(12)} | {prato.descricao}")
            
    def aplicar_desconto(self):
        self._preco *= 0.92
        self._preco = round(self._preco, 2)
        return self._preco  
    
            
            
            
            
    
