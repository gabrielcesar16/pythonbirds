class Pessoa:
    def __init__(self, nome = None, idade = 23):
        self.idade = idade
        self.nome = nome


    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '  main  ':
    p = Pessoa('Gabriel')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
