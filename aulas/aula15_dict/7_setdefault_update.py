# AULA 15 - ESTRUTURA DE DADOS - DICIONÁRIO - MÉTODOS - SETDEFAULT / UPDATE
# Data: 14/01/2024

import os


os.system('cls')

# Título
print('=' * 100)
print('DICT - MÉTODOS - SETDEFAULT / UPDATE')
print('-' * 100)

# Insere uma chave no dicionário com um valor padrão somente se a chave ainda não existir. 
# Retorna o valor da chave especificada.
print('Sintaxe 1: dicionário.setdefault(chave, valor_padrão)')
print('-' * 100)

# Atualiza o dicionário com as chaves e valores de outro dicionário ou de pares chave-valor fornecidos.
print('Sintaxe 2: dicionário.update(variável)')
print('=' * 100)
print()

# Dict
my_dict = {}

# Menu
while True:
    print('=' * 100)
    print('Menú de Opções:')
    print('-' * 100)
    print('1. Adicionar um par chave-valor.')
    print('-' * 100)
    print('2. Definir valor padrão para uma chave ".setdefault()".')
    print('-' * 100)
    print('3. Atualizar o dicionário ".update()".')
    print('-' * 100)
    print('4. Mostrar dicionário atual.')
    print('-' * 100)
    print('5. Sair.')
    print('=' * 100)
    print()

    # Iteração usuário
    print('=' * 100)
    opcao = input('Escolha uma opção (1-5): ')
    print('=' * 100)
    print()

    # Adicionar par chave-valor
    if opcao == '1':
        print('=' * 100)
        chave = input('Digite a chave: ')
        print('-' * 100)
        valor = input('Digite o valor: ')
        my_dict[chave] = valor
        print('-' * 100)
        print(f'Par {chave}: {valor} adicionado.')
        print('=' * 100)
        print()

    # Definir valor padrão para uma chave ".setdefault(chave, valor_padrão)"
    elif opcao == '2':
        print('=' * 100)
        chave = input('Digite a chave para definir um valor padrão: ')
        print('-' * 100)
        valor_padrao = input('Digite o valor padrão: ')
        print('-' * 100)
        valor_existente = my_dict.setdefault(chave, valor_padrao)
        print(f'Valor para a chave: "{chave}": {valor_existente}')
        print('=' * 100)
        print()

    # Atualizar o dict 
    elif opcao == '3':
        print('=' * 100)
        pares = input('Digite os novos pares chave valor'\
                            'no formato: "chave_1: valor_1, chave_2: valor_2": ')
        print('-' * 100)

        # Divisão dos pares em lista ".split(',')"
        pares_lista = pares.split(', ')
        att_dict = {}

        # Iteração entre pares chave-valor da lista
        for par in pares_lista:
            chave, valor = par.split(':')
            att_dict[chave] = valor
        
        # Atualização do dict ".update(variável)"
        my_dict.update(att_dict)
        print(f'Dicionário atualizado: {my_dict}')
        print('=' * 100)
        print()
    
    # Mostrar dict atualizado
    elif opcao == '4':
        
        # Condição de existência
        if my_dict:
            print('=' * 100)
            print('Dicionário atualizado:', my_dict)
            print('=' * 100)
            print()
        else:
            print('=' * 100)
            print('O dicionário está vazio. Adicione itens primeiro.')
            print('=' * 100)
            print()
            
    # Encerrar o programa
    elif opcao == '5':
        print('=' * 100)
        print('Encerrando o sistema...')
        print('=' * 100)
        print()
        break
    
    else:
        print('=' * 100)
        print('Opção inválida. Tente novamente.')
        print('=' * 100)
        print()