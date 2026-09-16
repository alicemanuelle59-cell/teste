# ============================================================
# SISTEMA DE BIBLIOTECA - POO COM PYTHON
# ============================================================


# ============================================================
# ETAPA 1, 2 e 3
# Classe Livro
# Abstração + Encapsulamento
# ============================================================

class Livro:

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

        # Atributo privado
        self.__disponivel = True

    def exibir_dados(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
        print(f"Disponível: {self.__disponivel}")

    # Método para emprestar livro
    def emprestar(self):

        if self.__disponivel:
            self.__disponivel = False
            print("Livro emprestado com sucesso!")
            return True

        else:
            print("Livro indisponível!")
            return False

    # Método para devolver livro
    def devolver(self):

        if not self.__disponivel:
            self.__disponivel = True
            print("Livro devolvido com sucesso!")
            return True

        else:
            print("O livro já está disponível!")
            return False

    # Método para verificar disponibilidade
    def verificar_disponibilidade(self):
        return self.__disponivel


# ============================================================
# ETAPA 2
# Classe Usuario
# Abstração
# ============================================================

class Usuario:

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")

    # Método que será sobrescrito pelas classes filhas
    def apresentar(self):
        print(f"Usuário: {self.nome}")


# ============================================================
# ETAPA 4
# Herança
# Classes Aluno e Professor
# ============================================================

class Aluno(Usuario):

    def __init__(self, nome, matricula, curso):

        # Aproveita os atributos da classe Usuario
        super().__init__(nome, matricula)

        self.curso = curso

    # ========================================================
    # ETAPA 5 - Polimorfismo
    # ========================================================

    def apresentar(self):
        print(f"Aluno: {self.nome} - Curso: {self.curso}")


class Professor(Usuario):

    def __init__(self, nome, matricula, disciplina):

        # Aproveita os atributos da classe Usuario
        super().__init__(nome, matricula)

        self.disciplina = disciplina

    # ========================================================
    # ETAPA 5 - Polimorfismo
    # ========================================================

    def apresentar(self):
        print(
            f"Professor: {self.nome} - "
            f"Disciplina: {self.disciplina}"
        )


# ============================================================
# DESAFIO EXTRA
# Classe Funcionario
# Herança + Polimorfismo
# ============================================================

class Funcionario(Usuario):

    def __init__(self, nome, matricula, cargo):

        super().__init__(nome, matricula)

        self.cargo = cargo

    def apresentar(self):
        print(
            f"Funcionário: {self.nome} - "
            f"Cargo: {self.cargo}"
        )


# ============================================================
# ETAPA 6
# Classe Biblioteca
# ============================================================

class Biblioteca:

    def __init__(self):

        # Atributos privados
        self.__livros = []
        self.__usuarios = []

    # ========================================================
    # ADICIONAR LIVRO
    # ========================================================

    def adicionar_livro(self, livro):

        self.__livros.append(livro)

        print("Livro cadastrado com sucesso!")

    # ========================================================
    # ADICIONAR USUÁRIO
    # ========================================================

    def adicionar_usuario(self, usuario):

        self.__usuarios.append(usuario)

        print("Usuário cadastrado com sucesso!")

    # ========================================================
    # LISTAR LIVROS
    # ========================================================

    def listar_livros(self):

        if len(self.__livros) == 0:
            print("Nenhum livro cadastrado.")
            return

        print("\n========== LIVROS ==========")

        for i, livro in enumerate(self.__livros, start=1):

            print(f"\nLivro {i}")
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Ano: {livro.ano}")

            if livro.verificar_disponibilidade():
                print("Status: Disponível")
            else:
                print("Status: Emprestado")

    # ========================================================
    # LISTAR USUÁRIOS
    # ========================================================

    def listar_usuarios(self):

        if len(self.__usuarios) == 0:
            print("Nenhum usuário cadastrado.")
            return

        print("\n========== USUÁRIOS ==========")

        for i, usuario in enumerate(self.__usuarios, start=1):

            print(f"\nUsuário {i}")

            # POLIMORFISMO
            usuario.apresentar()

            print(f"Matrícula: {usuario.matricula}")

    # ========================================================
    # PROCURAR LIVRO
    # ========================================================

    def procurar_livro(self, titulo):

        for livro in self.__livros:

            if livro.titulo.lower() == titulo.lower():
                return livro

        return None

    # ========================================================
    # PROCURAR USUÁRIO
    # ========================================================

    def procurar_usuario(self, matricula):

        for usuario in self.__usuarios:

            if usuario.matricula == matricula:
                return usuario

        return None

    # ========================================================
    # REALIZAR EMPRÉSTIMO
    # ========================================================

    def realizar_emprestimo(self):

        if len(self.__livros) == 0:
            print("Não existem livros cadastrados.")
            return

        if len(self.__usuarios) == 0:
            print("Não existem usuários cadastrados.")
            return

        print("\n========== EMPRÉSTIMO ==========")

        titulo = input("Digite o título do livro: ")

        livro = self.procurar_livro(titulo)

        if livro is None:
            print("Livro não encontrado!")
            return

        matricula = input("Digite a matrícula do usuário: ")

        usuario = self.procurar_usuario(matricula)

        if usuario is None:
            print("❌Usuário não encontrado!")
            return

        # Verifica se o livro está disponível
        if livro.verificar_disponibilidade():

            livro.emprestar()

            print(
                f"✅Empréstimo realizado para "
                f"{usuario.nome}!"
            )

        else:

            print("✔️Este livro já está emprestado.")

    # ========================================================
    # REALIZAR DEVOLUÇÃO
    # ========================================================

    def realizar_devolucao(self):

        if len(self.__livros) == 0:
            print("Não existem livros cadastrados.")
            return

        print("\n========== DEVOLUÇÃO ==========")

        titulo = input("📌Digite o título do livro: ")

        livro = self.procurar_livro(titulo)

        if livro is None:
            print("📌Livro não encontrado!")
            return

        livro.devolver()


# ============================================================
# ETAPA 7
# MENU DO SISTEMA
# ============================================================

biblioteca = Biblioteca()


while True:

    print("\n")
    print("===================================")
    print("       BIBLIOTECA POO")
    print("===================================")
    print("1 - 📚Cadastrar livro")
    print("2 - 👨‍🎓Cadastrar aluno")
    print("3 - 🧑‍🏫Cadastrar professor")
    print("4 - 🗒️Listar livros")
    print("5 - 📜Listar usuarios")
    print("6 - 📖Emprestar livro")
    print("7 - ↩️Devolver livro")
    print("8 - 👋Sair")
    print("===================================")

    opcao = input("👉Escolha uma opção: ")

    # ========================================================
    # 1 - CADASTRAR LIVRO
    # ========================================================

    if opcao == "1":

        print("\n========== CADASTRAR LIVRO ==========")

        titulo = input("📌Digite o título: ")
        autor = input("📌Digite o autor: ")

        try:
            ano = int(input("📌Digite o ano: "))
        except ValueError:
            print("📌Digite um ano válido!")
            continue

        livro = Livro(titulo, autor, ano)

        biblioteca.adicionar_livro(livro)

    # ========================================================
    # 2 - CADASTRAR ALUNO
    # ========================================================

    elif opcao == "2":

        print("\n========== CADASTRAR ALUNO ==========")

        nome = input("📌Digite o nome: ")
        matricula = input("📌Digite a matrícula: ")
        curso = input("📌Digite o curso: ")

        aluno = Aluno(nome, matricula, curso)

        biblioteca.adicionar_usuario(aluno)

    # ========================================================
    # 3 - CADASTRAR PROFESSOR
    # ========================================================

    elif opcao == "3":
        print("\n========== CADASTRAR PROFESSOR ==========")
        nome = input("📌Digite o nome: ")
        matricula = input("📌Digite a matrícula: ")
        disciplina = input("📌Digite a disciplina: ")
        professor = Professor(
            nome,
            matricula,
            disciplina
        )
        biblioteca.adicionar_usuario(professor)

    # ========================================================
    # 4 - LISTAR LIVROS
    elif opcao == "4":
        biblioteca.listar_livros()

    # 5 - LISTAR USUÁRIOS
    elif opcao == "5":
        biblioteca.listar_usuarios()

    # 6 - EMPRESTAR LIVRO
    elif opcao == "6":
        biblioteca.realizar_emprestimo()

    # 7 - DEVOLVER LIVRO
    elif opcao == "7":
        biblioteca.realizar_devolucao()

    # 8 - SAIR
    elif opcao == "8":
        print("\n👍Obrigado por usar o sistema!")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("❌Opção inválida! Tente novamente.")