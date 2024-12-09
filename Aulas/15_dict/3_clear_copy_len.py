# AULA 15 - ESTRUTURA DE DADOS - DICIONÁRIO - MÉTODOS - LEN / COPY / CLEAR
# Data: 09/12/2024

import os


os.system('cls')

# Título
print('=' * 80)
print('DICT - MÉTODOS - LEN / COPY / CLEAR')
print('-' * 80)
print('Sintaxe 1: variável = len(dicionário)')
print('-' * 80)
print('Sintaxe 2: variável = dicionário.copy()')
print('-' * 80)
print('Sintaxe 3: dicionário.clear()')
print('=' * 80)
print()

# Dicionário
my_dict = {}

# Menu
while True:
    print('=' * 80)
    print('Menu de opções:')
    print('=' * 80)
    print('1. Adicionar um par "chave-valor".')
    print('-' * 80)
    print('2. Mostrar o dicionário.')
    print('-' * 80)
    print('3. Mostrar o tamanho do dicionário (len).')
    print('-' * 80)
    print('4. Fazer uma cópia do dicionário (copy).')
    print('-' * 80)
    print('5. Limpar dicionário (clear).')
    print('-' * 80)
    print('6. Sair')
    print('=' * 80)
    print()

    # Iteração usuário
    print('=' * 80)
    option = input('Escolha uma opção (1-6): ')
    print('=' * 80)
    print()

    # Condição opção
    if option == '1':

        # Adição de par "chave-valor" ao dicionário
        print('=' * 80)
        chave = input('Digite a chave: ')

        # Validação para entrada de chave
        while not chave:
            print('-' * 80)
            print('A chave não pode ser vazia. Tente novamente.')
            print('-' * 80)
            chave = input(f'Digite a chave: ')

        print('-' * 80)
        valor = input('Digite o valor: ')

        # Validação para entrada de valor
        while not valor:
            print('-' * 80)
            print(f'O valor não pode ser vazio. Tente novamente.')
            print('-' * 80)
            valor = input('Digite o valor: ')
        
        print('-' * 80)
        my_dict[chave] = valor
        print(f'Par "{chave}: {valor}" adicionado.')
        print('=' * 80)
        print()
    
    elif option == '2':

        # Exibição do dicionário atual
        print('=' * 80)
        print(f'Dicionário atual: {my_dict}')
        print('=' * 80)
        print()
    
    elif option == '3':

        # Contagem do dicionário
        tamanho = len(my_dict)
        print('=' * 80)
        print(f'O dicionário tem {tamanho} elementos.')
        print('=' * 80)
        print()

    elif option == '4':

        # Cópia do dicionário
        copy = my_dict.copy()
        print('=' * 80)
        print(f'Cópia do dicionário: {copy}')
        print('=' * 80)
        print()

    elif option == '5':

        # Limpeza do dicionário
        my_dict.clear()
        print('=' * 80)
        print('Dicionário limpo.')
        print('=' * 80)
        print()
    
    elif option == '6':

        # Quebra do menu
        print('=' * 80)
        print('Encerrando o sistema.')
        print('=' * 80)
        print()
        break

    else:
        print('=' * 80)
        print('Opção inválida. Tente novamente.')
        print('=' * 80)
        print()