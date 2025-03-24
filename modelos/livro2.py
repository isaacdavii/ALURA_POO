class Livro:
    livros = []

    def __init__(self, titulo, autor, ano):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._disponivel = True
        self._emprestar = False
        Livro.livros.append(self)

    @property
    def titulo(self):
        return self._titulo
    @property
    def autor(self):
        return self._autor
    @property
    def ano(self):
        return self._ano
    @property
    def disponivel(self):
        return self._disponivel

    def alterar_estado(self):
        self._disponivel = not self._disponivel
        
    def emprestar(self):
        self._disponivel = False
        
    def devolver(self):
        self._disponivel = True

    def __str__(self):
        return f"{self._titulo.ljust(7)} | {self._autor.ljust(7)} | {self._ano} | {self._disponivel}"

    @classmethod
    def listar_livros(cls):
        print(f"{'Título'.ljust(20)} | {'Autor'.ljust(20)} | {'Ano'.ljust(7)} | {'Disponibilidade'} ")
        print("-" * 73)
        for livro in cls.livros:
            print(f"{livro.titulo.ljust(20)} | {livro.autor.ljust(20)} | {str(livro.ano).ljust(7)} | {livro.disponivel}")
        print()
        
    @staticmethod
    def verificar_disponibilidade():
        ano = int(input('Digite o ano de publicação: '))
        livros_disponiveis = [livro.titulo for livro in Livro.livros if livro.ano == ano and livro.disponivel]
        if livros_disponiveis:
            print("Livros disponíveis:", livros_disponiveis)
        else:
            print("Nenhum livro disponível")
        return livros_disponiveis

#livro1 = Livro("Senhor dos Aneis", "Tolkien", 1955)
#livro2 = Livro("O Hobbit", "J.R.R. Tolkien", 1937)
#livro3 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)
#livro4 = Livro("1984", "George Orwell", 1949)


#print(livro1)
#print(livro2)

#livro2.emprestar()
#livro2.devolver()
#livro3.emprestar()

#Livro.listar_livros()

#Livro.verificar_disponibilidade()




