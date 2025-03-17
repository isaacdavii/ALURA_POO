'''
Por fim, adicione uma propriedade chamada saudacao que retorna 
uma mensagem de saudação personalizada com base na profissão da pessoa.
'''

class Pessoa:
    pessoas = []
    
    def __init__(self, nome, idade, profissao):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao
        Pessoa.pessoas.append(self)
        
    @property
    def nome(self):
        return self._nome
    @property
    def idade(self):
        return self._idade
    @property
    def profissao(self):
        return self._profissao
    
    def __str__(self):
        return f'{self._nome} tem {self._idade} anos e é {self._profissao}.'
    
    def aniversario(self):
        self._idade += 1
    
    def saudacao(self):
        return f'Olá, {self._nome}! Vejo que você é um(a) {self._profissao}! Bem vindo!'
    
pessoa1 = Pessoa('João', 30, 'médico')
pessoa2 = Pessoa('Maria', 25, 'engenheiro')

print(pessoa1.saudacao())