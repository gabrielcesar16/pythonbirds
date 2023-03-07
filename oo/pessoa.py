class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 23):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    jose = Pessoa(nome="José")
    joao = Pessoa(jose, nome='João')
    print(id(jose))
    print(jose.nome)
    print(jose.idade)
    
    for filho in joao.filhos:
        print (f'Os filhos de João são : {filho.nome}')
