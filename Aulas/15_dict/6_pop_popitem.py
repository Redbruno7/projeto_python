# AULA 15 - ESTRUTURA DE DADOS - DICIONÁRIO - MÉTODOS - POP / POPITEM
# Data: 13/01/2024

import os


os.system('cls')

# Título
print('=' * 80)
print('DICT - MÉTODOS - POP / POPITEM')
print('-' * 80)
print('Sintaxe 1: dicionário.pop(key, default)')
print('-' * 80)
print('Sintaxe 2: dicionário.keys()')
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
print('2. Remover um item.')
print('-' * 80)
print('3. Remover o último item.')
print('-' * 80)
print('4. Mostrar dicionário atual.')
print('-' * 80)
print('5. Sair.')
print('=' * 80)
print()

# Looping Menu
while True:
    print('=' * 80)
    opcao = input('Escolha uma opção (1-5)')
    print('=' * 80)
    print()
        
    # Adicionar um par chave-valor
    if opcao == '1':
        print('=' * 80)
        chave = input('Digite a chave: ')
        print('-' * 80)
        valor = input('Digite o valor: ')
        print('-' * 80)
        my_dict[chave] = valor
        print(f'Par {chave}: {valor} adicionado.')
        print('=' * 80)
        print()
        
    # Remoção de item específico
    elif opcao == '2':
        
        # Condição de existência
        if my_dict:
            print('=' * 80)
            chave = input('Digite a chave do item que deseja remover: ')
            valor_removido = my_dict.pop(chave, 'Chave não encontrada')
            print('-' * 80)
            print(f'Item removido: {chave}: {valor_removido}')
            print('=' * 80)
            print()
        else:
            print('=' * 80)
            print('O dicionário está vazio. Adicione itens primeiro.')
            print('=' * 80)
            print()

    # Remoção do último item
    elif opcao == '3':
        
        # Condição de existência
        if my_dict:
            chave, valor = my_dict.popitem()
            print('=' * 80)
            print(f'Último item removido: {chave}: {valor}')
            print('=' * 80)
            print()
        else:
            print('=' * 80)
            print('O dicionário está vazio. Adicione itens primeiro.')
            print('=' * 80)
            print()
    
    # Dicionário atualizado
    elif opcao == '4':
        
        # Condição de existência
        if my_dict:
            print('=' * 80)
            print('Dicionário atualizado:', my_dict)
            print('=' * 80)
            print()
        else:
            print('=' * 80)
            print('O dicionário está vazio. Adicione itens primeiro.')
            print('=' * 80)
            print()
            
    # Encerrar o programa
    elif opcao == '5':
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