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


usuario1 = Aluno("Ana", "A001", "Informática")
usuario2 = Professor("Carlos", "P100", "Matemática")

usuario1.apresentar()
usuario2.apresentar()