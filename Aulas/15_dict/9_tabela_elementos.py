# AULA 15 - ESTRUTURA DE DADOS - DICIONÁRIO - EXEMPLO 1
# Data: 14/01/2024

import os


# Dict
elementos = {}

# List
tabela = []

# Menu
while True:
    os.system('cls')
    
    
    print('=' * 100)
    print('Menu de Opções')
    print('-' * 100)
    print('1. Adicionar um elemento na lista "list.append(dict)".')
    print('-' * 100)
    print('2. Remover elemento da tabela "del dict[key]"')
    print('-' * 100)
    print('3. Exibir a tabela detalhada.')
    print('-' * 100)
    print('4. Sair.')
    print('-' * 100)
    opcao = input('Digite uma opção (1-4): ').strip()
    print('=' * 100)
    print()
    
    # Adicionar elemento na lista "list.append(dict)".
    if opcao == '1':
        print('=' * 100)
        simbolo = input('Símbolo do elemento: ').strip().capitalize()
        print('-' * 100)
        nome = input('Nome do elemento: ').strip().capitalize()
        print('-' * 100)

        # Adicionar elemento no dicionário "dict[key] = value"
        elementos['Símbolo'] = simbolo
        elementos['Nome'] = nome
        
        # Adicionar uma cópia do dicionário à lista "list.append(dict.copy)".
        tabela.append(elementos.copy())
        print(f'Elemento {nome} ({simbolo}) adicionado à tabela.')
        print('-' * 100)
        print('Tabela atualizada:')
        print('-' * 100)
        print(tabela)
        print('=' * 100)
        print()
    
    # Remover elemento da tabela "list.remove(nome)"
    elif opcao == '2':
        print('=' * 100)
        remocao = input('Digite o nome do elemento que deseja remover: ').strip().capitalize()
        print('-' * 100)

        # Verificar existência de contato "key in dict"
        if remocao in elementos:
            del elementos[remocao]
            print(f'Elemento {remocao} removido.')
            print('=' * 100)
            print()
        else:
            print(f'Elemento {remocao} não encontrado na agenda.')
            print('=' * 100)
            print()
            
    # Mostrar tabela atualizada
    elif opcao == '3':
        print('=' * 100)
        print('Tabela detalhada:')
        
        # Iterar na lista "for i in list"
        for i in tabela:
            print('-' * 100)
            
            # Iterar no dicionário "for key, value in i.items()"
            for key, value in i.items():
                print(f'{key}: {value}')
        print('=' * 100)
        print()
        
    # Sair do sistema "break"
    elif opcao == '4':
        print('=' * 100)
        print('Sistema encerrado.')
        print('=' * 100)
        print()
        break
    
    # Condição de opção
    else:
        print('=' * 100)
        print('Opção inválida. Tente novamente.')
        print('=' * 100)
        print()
    
    # Continuar navegando
    print('=' * 100)
    input('Pressione "Enter" para continuar...')
    print('=' * 100)
    print()