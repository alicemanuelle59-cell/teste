class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def exibir_dados(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
        print(f"Disponível: {self.disponivel}")

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print("Livro emprestado com sucesso!")
        else:
            print("Livro indisponível!")

    def devolver(self):
        self.disponivel = True
        print("Livro devolvido com sucesso!")


livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("O Hobbit", "J. R. R. Tolkien", 1937)
livro3 = Livro("1984", "George Orwell", 1949)

livro1.exibir_dados()
print()

livro1.emprestar()
livro1.emprestar()
livro1.devolver()
