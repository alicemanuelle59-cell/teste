import tkinter as tk
from tkinter import ttk, messagebox


# ============================================================
# CLASSE LIVRO
# Encapsulamento
# ============================================================

class Livro:

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

        # Atributo privado
        self.__disponivel = True

    def exibir_dados(self):
        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Ano: {self.ano}\n"
            f"Disponível: {self.__disponivel}"
        )

    def emprestar(self):

        if self.__disponivel:
            self.__disponivel = False
            return True

        return False

    def devolver(self):

        if not self.__disponivel:
            self.__disponivel = True
            return True

        return False

    def verificar_disponibilidade(self):
        return self.__disponivel


# ============================================================
# CLASSE USUARIO
# Abstração
# ============================================================

class Usuario:

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def exibir_dados(self):
        return (
            f"Nome: {self.nome}\n"
            f"Matrícula: {self.matricula}"
        )

    def apresentar(self):
        return f"Usuário: {self.nome}"


# ============================================================
# CLASSE ALUNO
# Herança + Polimorfismo
# ============================================================

class Aluno(Usuario):

    def __init__(self, nome, matricula, curso):

        super().__init__(nome, matricula)

        self.curso = curso

    def apresentar(self):
        return f"Aluno: {self.nome} - Curso: {self.curso}"


# ============================================================
# CLASSE PROFESSOR
# Herança + Polimorfismo
# ============================================================

class Professor(Usuario):

    def __init__(self, nome, matricula, disciplina):

        super().__init__(nome, matricula)

        self.disciplina = disciplina

    def apresentar(self):
        return f"Professor: {self.nome} - Disciplina: {self.disciplina}"


# ============================================================
# CLASSE FUNCIONARIO
# Herança + Polimorfismo
# ============================================================

class Funcionario(Usuario):

    def __init__(self, nome, matricula, cargo):

        super().__init__(nome, matricula)

        self.cargo = cargo

    def apresentar(self):
        return f"Funcionário: {self.nome} - Cargo: {self.cargo}"


# ============================================================
# CLASSE BIBLIOTECA
# ============================================================

class Biblioteca:

    def __init__(self):

        self.__livros = []
        self.__usuarios = []

    def adicionar_livro(self, livro):

        self.__livros.append(livro)

    def adicionar_usuario(self, usuario):

        self.__usuarios.append(usuario)

    def listar_livros(self):

        return self.__livros

    def listar_usuarios(self):

        return self.__usuarios

    def procurar_livro(self, titulo):

        for livro in self.__livros:

            if livro.titulo.lower() == titulo.lower():
                return livro

        return None

    def procurar_usuario(self, matricula):

        for usuario in self.__usuarios:

            if usuario.matricula == matricula:
                return usuario

        return None

    def realizar_emprestimo(self, titulo, matricula):

        livro = self.procurar_livro(titulo)

        if livro is None:
            return "Livro não encontrado!"

        usuario = self.procurar_usuario(matricula)

        if usuario is None:
            return "Usuário não encontrado!"

        if livro.verificar_disponibilidade():

            livro.emprestar()

            return f"Empréstimo realizado para {usuario.nome}!"

        return "Este livro já está emprestado."

    def realizar_devolucao(self, titulo):

        livro = self.procurar_livro(titulo)

        if livro is None:
            return "Livro não encontrado!"

        if livro.devolver():

            return "Livro devolvido com sucesso!"

        return "O livro já está disponível."


# ============================================================
# INTERFACE GRÁFICA - TKINTER
# ============================================================

class InterfaceBiblioteca:

    def __init__(self, janela):

        self.janela = janela
        self.janela.title("Sistema de Biblioteca")
        self.janela.geometry("900x600")
        self.janela.resizable(False, False)

        self.biblioteca = Biblioteca()

        self.criar_interface()

    # ========================================================
    # INTERFACE PRINCIPAL
    # ========================================================

    def criar_interface(self):

        # Título
        titulo = tk.Label(
            self.janela,
            text="📚 SISTEMA DE BIBLIOTECA",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=20)

        # Frame dos botões
        frame_botoes = tk.Frame(self.janela)
        frame_botoes.pack(pady=10)

        tk.Button(
            frame_botoes,
            text="📚 Cadastrar Livro",
            width=20,
            height=2,
            command=self.cadastrar_livro
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            frame_botoes,
            text="👨‍🎓 Cadastrar Aluno",
            width=20,
            height=2,
            command=self.cadastrar_aluno
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            frame_botoes,
            text="🧑‍🏫 Cadastrar Professor",
            width=20,
            height=2,
            command=self.cadastrar_professor
        ).grid(row=0, column=2, padx=5, pady=5)

        tk.Button(
            frame_botoes,
            text="📖 Empréstimo",
            width=20,
            height=2,
            command=self.emprestar_livro
        ).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(
            frame_botoes,
            text="↩️ Devolução",
            width=20,
            height=2,
            command=self.devolver_livro
        ).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(
            frame_botoes,
            text="❌ Sair",
            width=20,
            height=2,
            command=self.janela.destroy
        ).grid(row=1, column=2, padx=5, pady=5)

        # ====================================================
        # TABELA DE LIVROS
        # ====================================================

        label_livros = tk.Label(
            self.janela,
            text="📚 Livros cadastrados",
            font=("Arial", 16, "bold")
        )

        label_livros.pack(pady=(20, 5))

        self.tabela_livros = ttk.Treeview(
            self.janela,
            columns=("titulo", "autor", "ano", "status"),
            show="headings",
            height=8
        )

        self.tabela_livros.heading("titulo", text="Título")
        self.tabela_livros.heading("autor", text="Autor")
        self.tabela_livros.heading("ano", text="Ano")
        self.tabela_livros.heading("status", text="Status")

        self.tabela_livros.column("titulo", width=250)
        self.tabela_livros.column("autor", width=200)
        self.tabela_livros.column("ano", width=100)
        self.tabela_livros.column("status", width=150)

        self.tabela_livros.pack()

    # ========================================================
    # CADASTRAR LIVRO
    # ========================================================

    def cadastrar_livro(self):

        janela = tk.Toplevel(self.janela)

        janela.title("Cadastrar Livro")
        janela.geometry("400x300")
        janela.resizable(False, False)

        tk.Label(
            janela,
            text="Cadastrar Livro",
            font=("Arial", 18, "bold")
        ).pack(pady=15)

        tk.Label(janela, text="Título:").pack()

        entrada_titulo = tk.Entry(janela, width=40)
        entrada_titulo.pack(pady=5)

        tk.Label(janela, text="Autor:").pack()

        entrada_autor = tk.Entry(janela, width=40)
        entrada_autor.pack(pady=5)

        tk.Label(janela, text="Ano:").pack()

        entrada_ano = tk.Entry(janela, width=40)
        entrada_ano.pack(pady=5)

        def salvar():

            titulo = entrada_titulo.get()
            autor = entrada_autor.get()
            ano = entrada_ano.get()

            if titulo == "" or autor == "" or ano == "":
                messagebox.showwarning(
                    "Atenção",
                    "Preencha todos os campos!"
                )
                return

            try:
                ano = int(ano)
            except ValueError:
                messagebox.showerror(
                    "Erro",
                    "Digite um ano válido!"
                )
                return

            livro = Livro(titulo, autor, ano)

            self.biblioteca.adicionar_livro(livro)

            self.atualizar_tabela()

            messagebox.showinfo(
                "Sucesso",
                "Livro cadastrado com sucesso!"
            )

            janela.destroy()

        tk.Button(
            janela,
            text="Cadastrar",
            width=20,
            command=salvar
        ).pack(pady=15)

    # ========================================================
    # CADASTRAR ALUNO
    # ========================================================

    def cadastrar_aluno(self):

        janela = tk.Toplevel(self.janela)

        janela.title("Cadastrar Aluno")
        janela.geometry("400x350")
        janela.resizable(False, False)

        tk.Label(
            janela,
            text="Cadastrar Aluno",
            font=("Arial", 18, "bold")
        ).pack(pady=15)

        tk.Label(janela, text="Nome:").pack()

        nome = tk.Entry(janela, width=40)
        nome.pack(pady=5)

        tk.Label(janela, text="Matrícula:").pack()

        matricula = tk.Entry(janela, width=40)
        matricula.pack(pady=5)

        tk.Label(janela, text="Curso:").pack()

        curso = tk.Entry(janela, width=40)
        curso.pack(pady=5)

        def salvar():

            if (
                nome.get() == ""
                or matricula.get() == ""
                or curso.get() == ""
            ):
                messagebox.showwarning(
                    "Atenção",
                    "Preencha todos os campos!"
                )
                return

            aluno = Aluno(
                nome.get(),
                matricula.get(),
                curso.get()
            )

            self.biblioteca.adicionar_usuario(aluno)

            messagebox.showinfo(
                "Sucesso",
                "Aluno cadastrado com sucesso!"
            )

            janela.destroy()

        tk.Button(
            janela,
            text="Cadastrar",
            width=20,
            command=salvar
        ).pack(pady=15)

    # ========================================================
    # CADASTRAR PROFESSOR
    # ========================================================

    def cadastrar_professor(self):

        janela = tk.Toplevel(self.janela)

        janela.title("Cadastrar Professor")
        janela.geometry("400x350")
        janela.resizable(False, False)

        tk.Label(
            janela,
            text="Cadastrar Professor",
            font=("Arial", 18, "bold")
        ).pack(pady=15)

        tk.Label(janela, text="Nome:").pack()

        nome = tk.Entry(janela, width=40)
        nome.pack(pady=5)

        tk.Label(janela, text="Matrícula:").pack()

        matricula = tk.Entry(janela, width=40)
        matricula.pack(pady=5)

        tk.Label(janela, text="Disciplina:").pack()

        disciplina = tk.Entry(janela, width=40)
        disciplina.pack(pady=5)

        def salvar():

            if (
                nome.get() == ""
                or matricula.get() == ""
                or disciplina.get() == ""
            ):
                messagebox.showwarning(
                    "Atenção",
                    "Preencha todos os campos!"
                )
                return

            professor = Professor(
                nome.get(),
                matricula.get(),
                disciplina.get()
            )

            self.biblioteca.adicionar_usuario(professor)

            messagebox.showinfo(
                "Sucesso",
                "Professor cadastrado com sucesso!"
            )

            janela.destroy()

        tk.Button(
            janela,
            text="Cadastrar",
            width=20,
            command=salvar
        ).pack(pady=15)

    # ========================================================
    # EMPRÉSTIMO
    # ========================================================

    def emprestar_livro(self):

        janela = tk.Toplevel(self.janela)

        janela.title("Empréstimo de Livro")
        janela.geometry("400x300")
        janela.resizable(False, False)

        tk.Label(
            janela,
            text="📖 Empréstimo",
            font=("Arial", 18, "bold")
        ).pack(pady=15)

        tk.Label(janela, text="Título do livro:").pack()

        titulo = tk.Entry(janela, width=40)
        titulo.pack(pady=5)

        tk.Label(janela, text="Matrícula do usuário:").pack()

        matricula = tk.Entry(janela, width=40)
        matricula.pack(pady=5)

        def realizar():

            resultado = self.biblioteca.realizar_emprestimo(
                titulo.get(),
                matricula.get()
            )

            messagebox.showinfo(
                "Empréstimo",
                resultado
            )

            self.atualizar_tabela()

            if "realizado" in resultado:
                janela.destroy()

        tk.Button(
            janela,
            text="Realizar empréstimo",
            width=25,
            command=realizar
        ).pack(pady=15)

    # ========================================================
    # DEVOLUÇÃO
    # ========================================================

    def devolver_livro(self):

        janela = tk.Toplevel(self.janela)

        janela.title("Devolução de Livro")
        janela.geometry("400x250")
        janela.resizable(False, False)

        tk.Label(
            janela,
            text="↩️ Devolução",
            font=("Arial", 18, "bold")
        ).pack(pady=15)

        tk.Label(
            janela,
            text="Título do livro:"
        ).pack()

        titulo = tk.Entry(
            janela,
            width=40
        )

        titulo.pack(pady=10)

        def realizar():

            resultado = self.biblioteca.realizar_devolucao(
                titulo.get()
            )

            messagebox.showinfo(
                "Devolução",
                resultado
            )

            self.atualizar_tabela()

            if "sucesso" in resultado:
                janela.destroy()

        tk.Button(
            janela,
            text="Devolver livro",
            width=25,
            command=realizar
        ).pack(pady=15)

    # ========================================================
    # ATUALIZAR TABELA
    # ========================================================

    def atualizar_tabela(self):

        # Limpa a tabela
        for item in self.tabela_livros.get_children():
            self.tabela_livros.delete(item)

        # Coloca novamente os livros
        for livro in self.biblioteca.listar_livros():

            if livro.verificar_disponibilidade():
                status = "Disponível"
            else:
                status = "Emprestado"

            self.tabela_livros.insert(
                "",
                "end",
                values=(
                    livro.titulo,
                    livro.autor,
                    livro.ano,
                    status
                )
            )


# ============================================================
# INICIAR PROGRAMA
# ============================================================

janela = tk.Tk()

app = InterfaceBiblioteca(janela)

janela.mainloop()