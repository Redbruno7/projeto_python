# AULA 15 - ESTRUTURA DE DADOS - DICIONÁRIO - MÉTODOS - DEL / IN / NOT IN
# Data: 14/01/2024

import os


# Título
print('=' * 100)
print('DICT - MÉTODOS - DEL / IN / NOT IN')
print('-' * 100)

# Remove chave e seu valor de um dicionário.
print('Sintaxe 1: del dicionário[chave]')
print('-' * 100)

# Verifica se uma chave existe no dicionário. Retorna valor booleano.
print('Sintaxe 2: chave in dicionário')
print('=' * 100)
print()

# Verifica se uma chave NÃO existe no dicionário. Retorna valor booleano.
print('Sintaxe 2: chave not in dicionário')
print('=' * 100)
print()

# Dict
agenda = {
    'Jojo': '99196-3030',
    'Dio': '99196-5050',
    'Jolyne': '99196-6060',
    'Lisa Lisa': '99196-7070',
    'Speedwagon': '99196-8080',
    'Zeppeli': '99196-9090',
    'Suzie Q.': '99196-0000'
}

# Primeiro teste "key in dict":
if 'Jojo' in agenda:
    print('=' * 100)
    print('Primeiro teste: Verificando se Jojo está no dicionário.')
    print('-' * 100)
    print('Verdadeiro! Jojo está no dicionário.')
    print('=' * 100)
    print()
else:
    print('=' * 100)
    print('Primeiro teste: Verificando se Jojo está no dicionário.')
    print('-' * 100)
    print('Falso! Jojo não está no dicionário.')
    print('=' * 100)
    print()
    
# Segundo teste "key not in dict":
if 'John' not in agenda:
    print('=' * 100)
    print('Segundo teste: Verificando se John não está no dicionário.')
    print('-' * 100)
    print('Verdadeiro! John não está no dicionário.')
    print('=' * 100)
    print()
else:
    print('=' * 100)
    print('Segundo teste: Verificando se John não está no dicionário.')
    print('-' * 100)
    print('Falso! Jojo está no dicionário.')
    print('=' * 100)
    print()   

# Início
while True:
    os.system('cls')


    print('=' * 100)
    print('Agenda de Contatos:')
    print('-' * 100)
    for nome, telefone in agenda.items():
        print(f'{nome}: {telefone}')
    print('=' * 100)
    print()     

    # Menu
    print('=' * 100)
    print('Menú de Opções:')
    print('-' * 100)
    print('1. Adicionar um contato. "dict[key] = value"')
    print('-' * 100)
    print('2. Remover um contato "del dict[key]".')
    print('-' * 100)
    print('3. Verificar contato específico "key in dict / key not in dict"')
    print('-' * 100)
    print('4. Mostrar agenda .')
    print('-' * 100)
    print('5. Sair.')
    print('=' * 100)
    print()

    # Iteração usuário
    print('=' * 100)
    opcao = input('Escolha uma opção (1-5): ')
    print('=' * 100)
    print()

    # Adicionar contato "dict[key] = value"
    if opcao == '1':
        print('=' * 100)
        nome = input('Digite o nome do contato: ')
        print('-' * 100)
        numero = input('Digite o número: ')
        agenda[nome] = numero
        print('-' * 100)
        print(f'Contato {nome}: {numero} adicionado.')
        print('=' * 100)
        print()

    # Remover contato "del dict[key]"
    elif opcao == '2':
        print('=' * 100)
        nome = input('Digite o nome do contato que deseja remover: ')
        print('-' * 100)

        # Verificar existência de contato "key in dict"
        if nome in agenda:
            del agenda[nome]
            print(f'Contato {nome} removido.')
            print('=' * 100)
            print()
        else:
            print(f'Contato {nome} não encontrado na agenda.')
            print('=' * 100)
            print()

    # Verificar contato "key in dict / key not in dict"
    elif opcao == '3':
        print('=' * 100)
        nome = input('Digite o nome do contato que deseja verificar: ')
        print('-' * 100)
        if nome in agenda:
            print(f'Contato encontrado - {nome}: {agenda[nome]}')
            print('=' * 100)
            print()
        else:
            print(f'Contato {nome} não encontrado na agenda.')
            print('=' * 100)
            print()

    # Mostrar agenda atualizada
    elif opcao == '4':
        print('=' * 100)
        print('Agenda atualizada:')
        print('-' * 100)
        print(agenda)
        print('=' * 100)
        print()

    # Sair "break"
    elif opcao == '5':
        print('=' * 100)
        print('Encerrando o sistema...')
        print('=' * 100)
        print()
        break
    
    # Condição para opção
    else:
        print('=' * 100)
        print('Opção inválida. Tente novamente.')
        print('=' * 100)
        print()
    
    print('=' * 100)
    input('Pressione "Enter" para continuar...')
    print('=' * 100)
    print()