class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


class Aluno(Usuario):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula)
        self.curso = curso


class Professor(Usuario):
    def __init__(self, nome, matricula, disciplina):
        super().__init__(nome, matricula)
        self.disciplina = disciplina


aluno1 = Aluno("Ana", "A001", "Informática")
prof1 = Professor("Carlos", "P100", "Matemática")

print(f"Aluno: {aluno1.nome}")
print(f"Matrícula: {aluno1.matricula}")
print(f"Curso: {aluno1.curso}")

print()

print(f"Professor: {prof1.nome}")
print(f"Matrícula: {prof1.matricula}")
print(f"Disciplina: {prof1.disciplina}")