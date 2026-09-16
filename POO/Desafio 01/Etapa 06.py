class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__usuarios = []

    def adicionar_livro(self, livro):
        self.__livros.append(livro)
        print("Livro cadastrado com sucesso!")

    def adicionar_usuario(self, usuario):
        self.__usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")

    def listar_livros(self):
        print("\n---------- LIVROS -------------")

        if not self.__livros:
            print("Nenhum livro cadastrado.")
            return

        for i, livro in enumerate(self.__livros, start=1):
            status = "Disponível" if livro.verificar_disponibilidade() else "Emprestado"

            print(f"{i} - {livro.titulo}")
            print(f"    Autor: {livro.autor}")
            print(f"    Ano: {livro.ano}")
            print(f"    Status: {status}")

    def listar_usuarios(self):
        print("\n--- USUÁRIOS ---")

        if not self.__usuarios:
            print("Nenhum usuário cadastrado.")
            return

        for usuario in self.__usuarios:
            usuario.apresentar()

    def realizar_emprestimo(self, livro):
        livro.emprestar()

    def realizar_devolucao(self, livro):
        livro.devolver()