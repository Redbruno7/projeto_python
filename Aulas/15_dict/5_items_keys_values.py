# AULA 15 - ESTRUTURA DE DADOS - DICIONÁRIO
# Data: 13/01/2024

import os


os.system('cls')

# Título
print('=' * 80)
print('DICT - MÉTODOS - ITEMS / KEYS / VALUES')
print('-' * 80)
print('Sintaxe 1: dicionário.items()')
print('-' * 80)
print('Sintaxe 2: dicionário.keys()')
print('-' * 80)
print('Sintaxe 3: dicionário.values()')
print('=' * 80)
print()

# Dict
my_dict = {}

# Menu
print('=' * 80)
print('Menú de Opções:')
print('-' * 80)
print('1. Adicionar um par chave-valor.')
print('-' * 80)
print('2. Mostrar chaves do dicionário.')
print('-' * 80)
print('3. Mostrar valores do dicionário.')
print('-' * 80)
print('4. Mostrar itens do dicionário.')
print('-' * 80)
print('5. Sair.')
print('=' * 80)
print()

# Looping menu
while True:
    
    # Iteração usuário
    print('=' * 80)
    opcao = input('Escolha uma opção (1-5): ')
    print('=' * 80)
    print()
    
    # Condição opção
    if opcao == '1':
        
        # Adicionar par chave-valor
        print('=' * 80)
        chave = input('Digite a chave: ')
        print('-' * 80)
        valor = input('Digite o valor: ')
        my_dict[chave] = valor
        print('-' * 80)
        print(f'Par "{chave}: {valor}" adicionado.')
        print('=' * 80)
        print()

    elif opcao == '2':
        
        # Mostrar chaves do dicionário
        if my_dict:
            print('=' * 80)
            print('Chaves do dicionário:', my_dict.keys())
            print('=' * 80)
            print()
        else:
            print('=' * 80)
            print('O dicionário está vazio. Adicione itens primeiro.')
            print('=' * 80)
            print()
        
    elif opcao == '3':
        
        # Mostrar valores do dicionário
        if my_dict:
            print('=' * 80)
            print('Valores do dicionário:', my_dict.values())
            print('=' * 80)
            print()
        else:
            print('=' * 80)
            print('O dicionário está vazio. Adicione itens primeiro.')
            print('=' * 80)
            print()    
        
    elif opcao == '4':
        
        # Mostras os itens (chave-valor) do dicionário
        if my_dict:
            print('=' * 80)
            print('Itens do dicionário:', my_dict.items())
            print('=' * 80)
            print()
        else:
            print('=' * 80)
            print('O dicionário está vazio. Adicione itens primeiro.')
            print('=' * 80)
            print()    

    elif opcao == '5':
        
        # Sair
        print('=' * 80)
        print('Encerrando o sistema...')
        print('=' * 80)
        print()
        break

    else:
        print('=' * 80)
        print('Opção inválida. Tente novamente.')
        print('=' * 80)
        print()