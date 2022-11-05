from typing_extensions import Self


class Professor: 

    def __init__(self,nome,qalunos):
        self.nome = nome
        self.qalunos = qalunos     

    def imprimir(self):
        print("Meu nome é: ",self.nome)
        print("tenho ",self.qalunos," Alunos")

    def adicionaraluno(self,alunos):
        self.qalunos += alunos

    def get_nome(self):
        return self.nome

    def set_nome(self,n_nome):
        n_nome = str
        self.nome = n_nome

    def get_qalunos(self):
        return self.qalunos

    def set_qalunos(self,alunos):
        alunos = int
        self.qalunos = alunos

p1 = Professor(input("Digite seu nome: "),int(input("digite quantos alunos: ")))
p1.get_nome()
p1.get_qalunos()
p1.adicionaraluno(int(input("digite quantos alunos quer adicionar")))


p2 = Professor(input("Digite seu nome: "),int(input("digite quantos alunos: ")))
p2.get_nome()
p2.get_qalunos()
p2.adicionaraluno(int(input("digite quantos alunos quer adicionar")))

p1.imprimir()
p2.imprimir()