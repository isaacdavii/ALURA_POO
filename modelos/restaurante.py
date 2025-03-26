# Aqui manteremos as classes que representam os modelos de dados do restaurante
# Classe é uma forma de organizar o código, ela é um molde para criar objetos
# As classes são compostas por atributos e métodos
# Métodos são funções que pertencem a uma classe
# Atributos são variáveis que pertencem a uma classe
# self é uma referência ao objeto que está sendo criado

from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:  # Sempre que criar uma classe usar a letra maiúscula
    restaurantes = []

    def __init__(self, nome, categoria):    
        self._nome = (nome.title())  # title() = Deixa a primeira letra de cada palavra em maiúscula
        self._categoria = (categoria.title())
        self._ativo = False  # Atributo privado colocando '__' antes do nome
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):  # Método especial que retorna uma string
        return f"{self._nome} | {self._categoria}"
    
    @classmethod  # Decorador que transforma o método em um método de classe
    def listar_restaurantes(cls):  # Método que lista os restaurantes
        print(f"{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(10)} | {'Status'}")
        print("-" * 65)
        for restaurante in cls.restaurantes:
            print(f"{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(10)} | {restaurante.ativo}")

    @property   # Decorador que transforma o método em uma propriedade
                # Propriedade é um método que se comporta como um atributo
                # Modifica como um atributo é lido
    def ativo(self):
        return "ON" if self._ativo else "OFF"
    @property
    def nome(self):
        return self._nome
    @property
    def categoria(self):
        return self._categoria
    @property
    def avaliacao(self):
        return self._avaliacao
    @property
    def cardapio(self):
        return self._cardapio
    
    def alterar_estado(self):
        self._ativo = not self._ativo
        
    def adicionar_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:            
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        return
        
    @property # Torna o método disponível para visualização como um atributo
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-' # Retorna um traço se não houver avaliações
        soma_notas = sum([avaliacao._nota for avaliacao in self._avaliacao]) # List Comprehension
        return print(f"A média das avaliações do restaurante {self._nome} é {round(soma_notas / len(self._avaliacao), 1):.2f}")
    
    def listar_avaliacoes(self):
        print(f"{'Cliente'.ljust(20)} | {'Nota'.ljust(10)}")
        print("-" * 30)
        for avaliacao in self._avaliacao:
            print(f"{avaliacao._cliente.ljust(20)} | {str(avaliacao._nota).ljust(10)}")
    
    def adicionar_item_cardapio(self, item):
        """
        Verificamos se o item é sublcasse de ItemCardapio, i.e, prato ou bebida
        Se sim, adicionamos
        """
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
        else:
            raise ValueError("O item não é um prato ou bebida")

    # Informa que é uma propriedade de leitura apenas
    def exibir_cardapio(self):
        print(f"Cardápio do Restaurante {self._nome}")
        # Essa função enumerate() vai devolver sempre duas informações: 
        # o índice que desejamos e o próprio item. Podemos escrever, por exemplo,
        # for i, item in enumerate(self._ cardapio, start=1). Aqui, i simboliza o índice.
        for i, item in enumerate(self._cardapio, start = 1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item.nome.ljust(20)} | Preço: R${str(item.preco).ljust(10)} | Descrição: {item.descricao} '
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item.nome.ljust(20)} | Preço: R${str(item.preco).ljust(10)} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)





# Instâncias da classe Restaurante
# restaurante_praca = Restaurante("praça", "Gourmet")
# restaurante_praca.alterar_estado()
# restaurante_pizza = Restaurante("pizza place", "Italiana")

# Esse chamado só é necessário se o método listar_restaurantes não for chamado
# restaurantes = [restaurante_praca, restaurante_pizza]

# print(dir(restaurante_pizza)) # dir() = Mostra os métodos e atributos do objeto
# print(vars(restaurante_praca)) # vars() = Mostra os atributos do objeto
# print(restaurantes[0].nome)
# print(restaurantes[1].categoria)

# Usado para chamar o método __str__
# print(restaurante_praca)
# print(restaurante_pizza)

# Restaurante.listar_restaurantes()  # Chamando o método listar_restaurantes

