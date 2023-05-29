class Pessoa:
    olhos = 2 #atributo de classe

    def __init__(self, *filhos, nome = None, idade = 23):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod #decorator
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - Numero de olhos da espécie: {cls.olhos}'
    
class Homem(Pessoa):
    pass 

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    jose = Mutante(nome="José")
    joao = Homem(jose, nome='João')
    print(id(jose))
    print(jose.nome)
    print(jose.idade)
    
    for filho in joao.filhos:
        print (f'Os filhos de João são : {filho.nome}')
    
    jose.sobrenome = 'Silva'
    del jose.filhos    
    print (jose.__dict__)
    print (joao.__dict__)
    print(joao.olhos)
    print(jose.olhos)
    print(Pessoa.nome_e_atributos_de_classe())
    pessoa = Pessoa ("Anonimo")
    print (isinstance(pessoa, Pessoa))
