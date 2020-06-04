""""# ''	Faça um programa em Python utilizando os conceitos de orientação a objetos para armazenar o nome, a idade, a altura e o peso de uma pessoa. Ao final o programa deve exibir os dados da pessoa e seu índice de massa corporal (IMC). O IMC é calculado dividindo o peso pela altura elevada ao quadrado. Ou seja, de forma mais simples, você multiplica sua altura por ela mesma e depois divide seu peso pelo resultado da última conta.'"""


class Pessoa(object):
    'Classe para calcular o IMC de uma pessoa'
    def __init__(self,nome,peso,altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.imc = 0

    def calcula(self):
        self.imc = self.peso/(self.altura*self.altura)
        #print "O IMC do %s eh %f" % (self.nome,imc)
        return self.imc
    def imprime(self):
        print "O IMC do %s eh %f" % (self.nome, self.calcula())