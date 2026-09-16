class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.__disponivel = True

    def exibir_dados(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print("Empréstimo realizado com sucesso!")
        else:
            print("Este livro já está emprestado.")

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print("Livro devolvido com sucesso!")
        else:
            print("Este livro já está disponível.")

    def verificar_disponibilidade(self):
        return self.__disponivel


class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def apresentar(self):
        print(f"Usuário: {self.nome}")


class Aluno(Usuario):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula)
        self.curso = curso

    def apresentar(self):
        print(f"Aluno: {self.nome} - Curso: {self.curso}")


class Professor(Usuario):
    def __init__(self, nome, matricula, disciplina):
        super().__init__(nome, matricula)
        self.disciplina = disciplina

    def apresentar(self):
        print(f"Professor: {self.nome} - Disciplina: {self.disciplina}")


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
        print("\n===== LIVROS =====")

        if not self.__livros:
            print("Nenhum livro cadastrado.")
            return

        for i, livro in enumerate(self.__livros, 1):
            status = "Disponível" if livro.verificar_disponibilidade() else "Emprestado"

            print(f"{i} - {livro.titulo}")
            print(f"    Autor: {livro.autor}")
            print(f"    Ano: {livro.ano}")
            print(f"    Status: {status}")

    def listar_usuarios(self):
        print("\n===== USUÁRIOS =====")

        if not self.__usuarios:
            print("Nenhum usuário cadastrado.")
            return

        for usuario in self.__usuarios:
            usuario.apresentar()

    def realizar_emprestimo(self):
        if not self.__livros:
            print("Nenhum livro cadastrado.")
            return

        self.listar_livros()

        try:
            numero = int(input("\nDigite o número do livro: "))

            if 1 <= numero <= len(self.__livros):
                livro = self.__livros[numero - 1]
                livro.emprestar()
            else:
                print("Livro inválido.")

        except ValueError:
            print("Digite um número válido.")

    def realizar_devolucao(self):
        if not self.__livros:
            print("Nenhum livro cadastrado.")
            return

        self.listar_livros()

        try:
            numero = int(input("\nDigite o número do livro: "))

            if 1 <= numero <= len(self.__livros):
                livro = self.__livros[numero - 1]
                livro.devolver()
            else:
                print("Livro inválido.")

        except ValueError:
            print("Digite um número válido.")


# Criando a biblioteca
biblioteca = Biblioteca()


# Livros
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("O Hobbit", "J. R. R. Tolkien", 1937)
livro3 = Livro("1984", "George Orwell", 1949)

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)


# Usuários
aluno = Aluno("Ana", "A001", "Desenvolvimento de Sistemas")
professor = Professor("Carlos", "P100", "Programação")

biblioteca.adicionar_usuario(aluno)
biblioteca.adicionar_usuario(professor)


# Menu
while True:

    print("\n==============================")
    print("       BIBLIOTECA POO")
    print("==============================")
    print("1 - Cadastrar livro")
    print("2 - Cadastrar aluno")
    print("3 - Cadastrar professor")
    print("4 - Listar livros")
    print("5 - Listar usuários")
    print("6 - Emprestar livro")
    print("7 - Devolver livro")
    print("0 - Sair")
    print("==============================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")
        ano = int(input("Digite o ano: "))

        livro = Livro(titulo, autor, ano)
        biblioteca.adicionar_livro(livro)

    elif opcao == "2":
        nome = input("Digite o nome: ")
        matricula = input("Digite a matrícula: ")
        curso = input("Digite o curso: ")

        aluno = Aluno(nome, matricula, curso)
        biblioteca.adicionar_usuario(aluno)

    elif opcao == "3":
        nome = input("Digite o nome: ")
        matricula = input("Digite a matrícula: ")
        disciplina = input("Digite a disciplina: ")

        professor = Professor(nome, matricula, disciplina)
        biblioteca.adicionar_usuario(professor)

    elif opcao == "4":
        biblioteca.listar_livros()

    elif opcao == "5":
        biblioteca.listar_usuarios()

    elif opcao == "6":
        biblioteca.realizar_emprestimo()

    elif opcao == "7":
        biblioteca.realizar_devolucao()

    elif opcao == "0":
        print("Obrigado por usar o sistema!")
        break

    else:
        print("Opção inválida! Tente novamente.")