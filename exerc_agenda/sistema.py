from exerc_agenda.lib.arquivo import *
from exerc_agenda.lib.interface import *
from time import sleep

arq = 'agendanova.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

cabeçalho('MENU PRINCIPAL')
while True:
    resposta = menu (['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho ('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = LeiaInt('Idade: ')
        telefone = str (input('Telefone: '))
        cadastrar(arq, nome, idade, telefone)
    elif resposta == 3:
        cabeçalho ('Saindo do sistema... Até logo')
    else:
        print ('\033[31mERRO!  Digite uma opção válida!\033[m')
    sleep(2)