class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.__disponivel = True

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print("Livro emprestado com sucesso!")
        else:
            print("Livro indisponível!")

    def devolver(self):
        self.__disponivel = True
        print("Livro devolvido com sucesso!")

    def verificar_disponibilidade(self):
        return self.__disponivel


livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)

print(livro1.verificar_disponibilidade())

livro1.emprestar()

print(livro1.verificar_disponibilidade())

livro1.devolver()

print(livro1.verificar_disponibilidade())