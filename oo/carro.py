class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor
    
    def calcular_velocidade(self):
        return self.motor.velocidade
    
    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()
    
    def calcular_direcao(self):
         return self.direcao.valor
    
    def girar_a_direita(self):
         return self.direcao.gira_direita()
    
    def girar_a_esquerda(self):
         return self.direcao.valor.gira_esquerda()

        
class Motor:
    def __init__(self):
        self.velocidade = 0
    
    def acelerar(self):
        self.velocidade+=1
    
    def frear(self):
        self.velocidade-=2
        self.velocidade = max(0, self.velocidade)
    
NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:
    
    rotacao_direita = {
        NORTE : LESTE, 
        LESTE : SUL, 
        SUL: OESTE, 
        OESTE: NORTE
        }
    
    rotacao_esquerda = {
        NORTE : OESTE, 
        LESTE : NORTE, 
        SUL: LESTE, 
        OESTE: SUL
        }

    def __init__(self):
        self.valor = NORTE
    
    def gira_direita(self):
        self.valor = self.rotacao_direita[self.valor]
    
    
    def gira_esquerda(self):
        self.valor = self.rotacao_esquerda[self.valor]
    
   