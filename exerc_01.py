#Faça um programa em Python utilizando os conceitos de listas e dicionário para armazenar o código, o nome, a altura e a idade de um grupo de pessoas. Ao final o programa deve exibir a quantidade de pessoas, a média das idades e a média das alturas das pessoas.#

grupo= list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['codigo'] = str(input('Digite o código: '))
    pessoa['nome'] = str(input('Digite o Nome:' ))
    pessoa['altura'] = float(input('Digite a altura: '))
    pessoa['idade'] = int (input('Digite a idade: '))
    soma1 += pessoa['altura']
    soma2 += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
media_idade = soma1 / len(grupo)
media_altura = soma2 / len(grupo)
print(f'B) A média das idades é: {media:5.2f}')
print(f'C) A média das altura é: {media:5.2f}')

print('<< ENCERRADO >>')

