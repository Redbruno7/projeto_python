# AULA 15 - ESTRUTURA DE DADOS - DICIONÁRIO - MÉTODOS - FROMKEYS / GET / JOIN
# Data: 09/12/2024

import os


os.system('cls')

# Título
print('=' * 80)
print('DICT - MÉTODOS - FROMKEYS / GET / JOIN')
print('-' * 80)

# Cria um novo dicionário com as chaves fornecidas e atribui o mesmo valor a todas elas.
print('Sintaxe 1: variável = dict.fromkeys(keys, value)')
print('-' * 80)

# Procura uma chave, se não tiver, assume-se valor padrão
print('Sintaxe 2: variável = dict.get(key, value_padrao)')
print('-' * 80)

# Junta uma sequência de strings com um separador definido
print('Sintaxe 3: variável = "separador".join(dict.keys())')
print('=' * 80)
print()

# Dicionário
my_dict = {}

# Menu
while True:
    print('=' * 80)
    print('Menu de opções:')
    print('-' * 80)
    print('1. Criar dicionário com "fromkeys()".')
    print('-' * 80)
    print('2. Buscar valor de uma chave com "get()".')
    print('-' * 80)
    print('3. Sair.')
    print('=' * 80)
    print()

    # Iteração usuário - opção
    print('=' * 80)
    option = input('Escolha uma opção (1-3): ')
    print('=' * 80)
    print()

    # Condição opção
    if option == '1':

        # Iteração usuário - dicionário
        print('=' * 80)
        entrada_chaves = input('Digite as chaves separadas por vígula: ')
        print('-' * 80)
        entrada_valor = input('Digite o valor padrão para as chaves: ')


        # Validação entrada usuário
        if not entrada_chaves.strip():
            print('-' * 80)
            print('Erro: Chaves não pode ser vazio.')
            print('=' * 80)
            print()
        elif not entrada_valor.strip():
            print('-' * 80)
            print('Erro: Valor padrão não pode ser vazio.')
            print('=' * 80)
            print()
        else:

            # Divisão das chaves
            chaves = entrada_chaves.split(',')

            # Remoção de espaços
            chaves = [chave.strip() for chave in chaves]

            # Criação dicionário
            my_dict = dict.fromkeys(chaves, entrada_valor.strip())
            print('=' * 80)
            print(f'Dicionário criado: {my_dict}')
            print('=' * 80)
            print()

    elif option == '2':

        # Verificação de criação do dicionário
        if my_dict:
            print('=' * 80)
            print('Chaves disponíveis:', ', '.join(my_dict.keys()))
            print('=' * 80)
            print()

            # Iteração usuário - busca
            print('=' * 80)
            elemento = input('Digite a chave que deseja buscar: ')

            # Busca elemento
            valor = my_dict.get(elemento, 'Chave não encontrada.')
            print('-' * 80)
            print(f'Valor para a chave "{elemento}": {valor}')
            print('=' * 80)
            print()
        else:
            print('=' * 80)
            print('Erro: Crie um dicionário primeiro.')
            print('=' * 80)
            print()

    elif option == '3':
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