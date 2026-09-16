class Usuario:
    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"E-mail: {self.email}")


usuario1 = Usuario("Ana", "A001", "ana@email.com")
usuario2 = Usuario("Carlos", "C002", "carlos@email.com")
usuario3 = Usuario("Mariana", "M003", "mariana@email.com")

usuario1.exibir_dados()
print()

usuario2.exibir_dados()
print()

usuario3.exibir_dados()