# AULA 15 - ESTRUTURA DE DADOS - DICIONÁRIO - EXEMPLO 2
# Data: 14/01/2024

import os


# Dict
elements = {}

# List
list = []

# Menu
while True:
    os.system('cls')
    
    
    print('=' * 100)
    print('Menu de Opções')
    print('-' * 100)
    print('1. Adicionar um elemento na lista "list.append(dict)".')
    print('-' * 100)
    print('2. Vizualizar elementos da lista.')
    print('-' * 100)
    print('3. Atualizar um elemento da lista "i[key] = value".')
    print('-' * 100)
    print('4. Remover um elemento da lista "list.remove(i)".')
    print('-' * 100)
    print('5. Sair.')
    print('-' * 100)
    option = input('Digite uma opção (1-5): ').strip()
    print('=' * 100)
    print()
    
    # Adicionar elemento
    if option == '1':
        print('=' * 100)
        symbol = input('Símbolo do elemento: ').strip().capitalize()
        print('-' * 100)
        name = input('Nome do elemento: ').strip().capitalize()
        print('-' * 100)

        # Adicionar elemento no dicionário "dict[key] = value"
        elements['Símbolo'] = symbol
        elements['Nome'] = name
        
        # Adicionar uma cópia do dicionário à lista "list.append(dict.copy)".
        list.append(elements.copy())
        print(f'Elemento {name} ({symbol}) adicionado à tabela.')
        print('=' * 100)
        print()
        
    # Mostrar tabela atualizada
    elif option == '2':
        print('=' * 100)
        print('Lista detalhada:')
        
        # Iterar na lista "for i in list"
        for i in list:
            print('-' * 100)
            
            # Iterar no dicionário "for key, value in i.items()"
            for key, value in i.items():
                print(f'{key}: {value}')
        print('=' * 100)
        print()
        
    # Atualizar elemento
    elif option == '3':
        print('=' * 100)
        symbol = input('Digite o símbolo do elemento que deseja atualizar: ').strip().capitalize()
        
        # Flag
        find = False
        
        # Iterar na lista "for i in list"
        for i in list:
            print('-' * 100)
            new_simbol = input(f'Digite o novo símbolo para'
            f' {symbol} (Deixe em branco para manter): ').strip().capitalize()
            print('-' * 100)
            new_name = input(f'Digite o novo nome para'
            f' {name} (Deixe em branco para manter): ').strip().capitalize()
            print('=' * 100)
            print()
            
            # Atualização "i[key] = value"
            if new_simbol:
                i['Símbolo'] = new_simbol
            if new_name:
                i['Nome'] = new_name
            
            # Converter flag
            find = True
            break
        
        if find:
            print('=' * 100)
            print('Elemento atualizado.')
            print('=' * 100)
            print()
        else:
            print('=' * 100)
            print('Elemento não encontrado.')
            print('=' * 100)
            print()
            
    # Remover elemento
    elif option == '4':
        print('=' * 100)
        symbol = input('Digite o símbolo do elemento que deseja remover: ').strip().capitalize()
        print('-' * 100)
        
        # Flag
        find = False
        
        # Iterar na lista "for i in list"
        for i in list:
            
            # Remover elemento da lista "list.remove(i)"
            if i['Símbolo'] == symbol:
                list.remove(i)
                
                # Converter flag
                find = True
                break
        
        # Condição de remoção
        if find:
            print('Elemento removido.')
        else:
            print('Elemento não encontrado.')
        
    # Sair do sistema "break"
    elif option == '5':
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