"""
Faça um programa em Python utilizando os conceitos de módulos e pacotes para criar um “conversor de moedas”.

O programa deve obter um valor em Real (R$) e converter esse valor para dólar, euro e libra esterlina.
"""
from cotação import *
valor1 = 0.17
valor2 = 0.19
valor3 = 0.15
valor4 = float(input('Quanto você tem em Real:?'))

print ('1 - Converter para Dólar')
print ('2 - Converter para Euro')
print ('3 - Converter para Libra')
print = float(input('Valor em Real'))
print ('0 - Sair')