from modelos.avaliacao import Avaliacao

class Restaurante:  # Sempre que criar uma classe usar a letra maiúscula
    restaurantes = []

    def __init__(self, nome, categoria):
        
        """
        O self ou this significa que para cara inicialiação dessa função eu quero que seja atribuída para cada restaurante
        Self ou this > referencia da instancia atual a que nos referimos
        E nome e categoria são as variáveis que irei inserir
        Ao pressionar F2 eu altero o nome e onde mais ele precisa ser mudado vai automaticamente
        
        O método __init__ é conhecido como o construtor da classe em Python. 
        Ele é automaticamente chamado quando uma nova instância da classe é criada e serve para realizar as inicializações necessárias nos atributos da instância. 
        O nome __init__ é uma abreviação de initialize (inicializar), e sua principal função é garantir que os atributos da instância tenham valores iniciais apropriados. 
        """
        
        self._nome = nome.title() # com [.title()] Mantemos a primeira letra maiúscula em todo nome que temos
        self.categoria = categoria
        self._ativo = False  # Ao colocar o underline(_) colocamos que é um atribut privado, i.e, que as pessoas não mudem o valor deles
        self._avaliacao = []  # Lista vazia para armazenar as avaliações #adicionado depois
        Restaurante.restaurantes.append(self)  # a fim de add o restaurante desejado na lista

    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod  # Método de classe, que não é de instância, mas sim da classe. Uso [cls]
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes: # Alterei Restaurante.restaurantes para cls.restaurantes
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property  # Modificar como um atributo é lido. Usado para op matemáticas ou agrupamento de muitos valores
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self): # É um método para o objeto, não para a classe
        self._ativo = not self._ativo
        
    @property    
    def media_avaliacoes(self):
        if not self._avaliacao:
            # mudarei de return 0 para uma string vazia
            return '-'
        else:
            return round(sum([avaliacao._nota for avaliacao in self._avaliacao]) / len(self._avaliacao), 1)
            # Round seria o arredondamento de casas decimais round(objeto, 2) para 2 casas decimais

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5: #Assim eu adiciono apenas as notas que estão nestes valores
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)




'''
Método utilizado no começo. Porém, na prática, será inserido pelo usuário

restaurante_pizza = Restaurante('pizzaria duBom', 'Pizzaria')
# restaurante_pizza._nome = 'Pizzaria JF' # Sempre que for alterar, temos que ter a mesma variável [_nome] por ex
restaurante_pizza._ativo = True
restaurante_mexicano = Restaurante('mechicano', 'Mexicano')
restaurante_mexicano.alternar_estado()
restaurante_praca = Restaurante('praça', 'Gourmet')

Restaurante.listar_restaurantes()  # Aqui eu chamo a função listar_restaurantes() que está dentro da classe Restaurante

'''

