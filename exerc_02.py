"""
Faça um programa em Python utilizando os conceitos de listas e dicionário para armazenar o código, o nome e o preço de um grupo de produtos. Ao final o programa deve exibir o valor médio dos produtos e os nomes dos produtos com preço superior a média da grupo.
"""

lista= list()
produto = dict()
soma = media = 0

while True:
    produto.clear()
    produto['codigo'] = str(input('Digite o Código do produto: '))
    produto['nome'] = str(input('Digite o nome do produto: ' ))
    produto['preço'] = float(input('Digite o preço do produto:R$ '))
    soma += produto['preço']
    lista.append(produto.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)

print(f'A) Ao todo temos {len(lista)} produtos cadastradas.')
media = soma / len(lista)

print(f'B) A média de preço dos produtos é: {media:5.2f}')
print(f'C) O produtos com preço acima da média são:')
for pr in lista:
    if pr ['preço'] > media:
        for k, v in pr.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')


