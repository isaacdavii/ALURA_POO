from modelos.livro2 import Livro

livro1 = Livro("Senhor dos Aneis", "Tolkien", 1955)
livro2 = Livro("O Hobbit", "J.R.R. Tolkien", 1937)
livro3 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)
livro4 = Livro("1984", "George Orwell", 1949)


def main():
    # Livro.listar_livros() #No início
    livro1.alterar_estado()
    # Livro.listar_livros() # Caso queira ver como ficou
    livro3.emprestar()
    Livro.listar_livros()
    Livro.verificar_disponibilidade()
    # print(livro1)


if __name__ == "__main__":
    main()
