from minhaClasse import Pessoa

nome = input ('Digite um nome: ')
idade =  int (input('Digite a idade: '))
peso = float(input('Digite o peso: '))
altura = float (input('Digite a altura: '))

p1 = Pessoa(nome,idade, peso, altura)

print ('_'*30)
print (p1.__repr__())
print (f'o IMC de {nome} é {peso / altura**2}')
