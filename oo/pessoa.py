class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '  main  ':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
