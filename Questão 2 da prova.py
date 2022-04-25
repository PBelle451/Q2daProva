class Aluno:
    def __init__(self, ra, nome):
        self.ra = ra
        self.nome = nome
    def get_nome(self):
        return self.nome
    def get_ra(self):
        return self.ra
    def set_ra(self, new):
        if isinstance(new, int):
            self.ra = new
        else:
            print("ERRO")
    def set_nome(self, new):
        if isinstance(new, str):
            self.nome = new
        else:
            print("ERRO")

class Curso:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        self.alunos = list()
    def get_nome(self):
        return self.nome
    def get_valor(self):
        return self.valor
    def set_nome(self, new):
        if isinstance(new, str):
            self. nome = new
        else:
            print("ERRO")
    def set_valor(self, valor):
        if isinstance(valor, float):
            self.valor = valor
        else:
            print("ERRO")
    def insere_aluno(self, aluno):
        self.alunos.append(aluno)

    def consulta_nome_alunos(self):
        if not self.alunos:
            print("A lista está vazia")
        else:
            for o_aluno in self.alunos:
                print(o_aluno.get_nome())

    def mostra_dados_curso(self):
        print("\nDados do curso:\nCurso: ", self.nome, "\nValor da mensalidade: R$", self.valor)

    def consulta_dados_alunos(self):
        if not self.alunos:
            print("A lista está vazia")
        else:
            for o_aluno in self.alunos:
                print(f"\nAluno: {o_aluno.get_nome()}\nRA: {o_aluno.get_ra()}\nCurso: {self.get_nome()}")

if __name__ == '__main__':
    a1 = Aluno(22103581, "Pedro")
    a2 = Aluno(68451231, "Gabriel")
    a3 = Aluno(65413274, "Luan")
    c1 = Curso("Ciência da Computação", 820.00)
    c2 = Curso("Psicologia", 2600.70)
    a4 = Aluno(98654645, "Dyulia")
    a5 = Aluno(56985412, "Clara")
    a6 = Aluno(32589864, "Johnny")
    c1.set_valor(1200.00)
    c1.insere_aluno(a1)
    c1.insere_aluno(a2)
    c1.insere_aluno(a3)
    c1.consulta_nome_alunos()
    c1.mostra_dados_curso()
    c2.insere_aluno(a4)
    c2.insere_aluno(a5)
    c2.insere_aluno(a6)
    c2.mostra_dados_curso()
    c2.consulta_nome_alunos()
    c1.consulta_dados_alunos()
    c2.consulta_dados_alunos()