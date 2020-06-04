class Pessoa(object):

    def __init__(self, n, i, p, a):
        self.nome = n
        self.idade = i
        self.peso = p
        self.altura = a


    def __repr__(self):
        return f'{self.nome} tem {self.idade} anos e pesa {self.peso}Kg e tem {self.altura}m. '

    def imc(self):
        imc = (p / (a*a))
        return f'{self.nome} tem imc de {imc}'

    def aniversario(self):
        self.idade += 1


