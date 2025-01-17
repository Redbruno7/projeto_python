# ATIVIDADE 009 - ATIVIDADE D
# ALUNO: BRUNO C. RODGERS
# Data: 14/01/2025
# Crie um programa que permita ao usuário cadastrar informações (valor) sobre 5 tipos de vinho (chave). 
# Para cada vinho, deve-se obter as seguintes informações: 
# º Nome do vinho
# º Tipo (como tinto, branco, rosé, etc.)
# º Teor alcoólico
# º Safra. 
# Exibir uma lista detalhada dos vinhos, com suas informações 
# Opção para modificar os dados de qualquer vinho previamente cadastrado. 
# Opção para relatório de quantos vinhos possuem teor alcoólico superior a 12%;
# E quantos pertencem a safras superiores ao ano de 2015, 
# Ordenar os vinhos por nome de forma crescente.


import os

# Limpar terminal
os.system('cls')

# Título
print('=' * 80)
print('DICIONÁRIO DE VINHOS')
print('=' * 80)
print()

# Dict "dict = {}"
wines_dict = {}

# Lista "list = []"
wines_list = []

# Iterar 5 vinhos "for i in range(value)"
for i in range(5):
    print('=' * 80)
    name = input(f'Nome do {i + 1}ª vinho: ').strip().capitalize()
    print('-' * 80)
    type = input(f'Tipo do vinho: ').strip().capitalize()
    print('-' * 80)
    content = float(input(f'Teor alcoólico: '))
    print('-' * 80)
    harvest = int(input(f'Safra do vinho: '))
    print('=' * 80)
    print()
    
    # Adicionar par cor-código ao dict "dict[key] = value"
    wines_dict['Nome'] = name
    wines_dict['Tipo'] = type
    wines_dict['Teor alcoólico'] = content
    wines_dict['Safra'] = harvest
    
    # Adicionar uma cópia dos dicts à lista "list.append(dict.copy())"
    wines_list.append(wines_dict.copy())

# Looping Menu "while True"
while True:
    
    # Limpar Terminal
    os.system('cls')
    
    # Exibir lista "for key, value in dict.items()"
    print('=' * 80)
    print('Lista atual: ')
    print('=' * 80)
    print()
    
    # Ordenar lista "a = sorted(list, key = lambda a: a['key'])"
    list_ordered = sorted(wines_list, key = lambda wine: wine['Nome'])
    
    # Iterar na lista "for i in list"
    print('=' * 80)
    for i in list_ordered:
        
        # Iterar no dict "for key, value in i.items()"
        for key, value in i.items():
            print(f'{key}: {value}')
        print('=' * 80)
    print()
    
    # Menu
    print('=' * 80)
    print('Menu de opções:')
    print('-' * 80)
    print('1. Modificar informação de um vinho.')
    print('-' * 80)
    print('2. Gerar relatório detalhado.')
    print('-' * 80)
    print('3. Sair.')
    print('-' * 80)
    option = input('Digite uma opção (1-3): ')
    print('=' * 80)
    print()
    
    # Modificar descrição da cor
    if option == '1':
        print('=' * 80)
        change = input(
            'Digite o nome do vinho para alterar suas informações: '
            ).strip().capitalize()
        print('-' * 80)
        
        # Flag busca "find = bool"
        find = False
        
        # Iterar na lista "for i in list"
        for i in list_ordered:
        
        # Condicionar existência "if i['key'] == a"
            if i['Nome'] == change:
                
                # Converter flag
                find = True
                
                # Itera usuário
                new_name = input(
                    'Digite um novo nome (aperte Enter para manter): '
                    ).strip().capitalize()
                print('-' * 80)
                new_type = input(
                    'Digite um novo tipo (aperte Enter para manter): '
                    ).strip().capitalize()
                print('-' * 80)
                new_content = float(
                    input('Digite um novo teor alcoólico'
                          ' (aperte Enter para manter): '))
                print('-' * 80)
                new_harvest = int(input(
                    'Digite um nova safra (aperte Enter para manter): '))
                print('-' * 80)
                    
                # Iterar no dict "for key, value in dict.items()"
                for key, value in wines_dict.items():
                    
                    # Modificar valores "dict['key'] = value"
                    i['Nome'] = new_name
                    i['Tipo'] = new_type
                    i['Teor alcoólico'] = new_content
                    i['Safra'] = new_harvest
                    
                print('informações atualizadas.')
                print('=' * 80)
                print()
                break
        else:
            print('Vinho não encontrado. Tente novamente.')
            print('=' * 80)
            print()

    # Relatório
    elif option == '2':

        # Iterar na lista "for i in list"
        print('=' * 80)
        for i in list_ordered:
        
        # Iterar no dict "for key, value in i.items()"
            for key, value in i.items():
                print(f'{key}: {value}')
            print('=' * 80)
        print()

        # Flag contador teor alcoólico "a = 0"
        content_count = 0

        # Iterar lista "for i in list"
        for i in list_ordered:

            # Condicionar existência teor alcoólico "if i['key'] > int"
            if i['Teor alcoólico'] > 12:

                # Somar flag "a += 1"
                content_count += 1
        
        # Flag contador safra "a = 0"
        harvest_count = 0

        # Iterar lista "for i in list"
        for i in list_ordered:

            # Condicionar existência safra "if i['key'] > int"
            if i['Safra'] > 2015:

                # Somar flag "a += 1"
                harvest_count += 1
                    
        # Saídas
        print('=' * 80)
        print(f'Quantidade de vinhos com teor alcoólico maior que 12.00%: {content_count}')
        print('-' * 80)
        print(f'Quantidade de vinhos com safra superior à 2015: {harvest_count}')
        print('=' * 80)
        print()

        # Identificar ferramentas com mais de uma palavra "a = [key for key in dict.keys if len(key.split()) > 1]"
        multi_tool_words = [
            key for key in wines_dict.keys() if len(key.split()) > 1]

        print('=' * 80)
        print(f'Quantidade de ferramentas com mais '
              f'de uma palavra no nome: {len(multi_tool_words)}.')
        print('=' * 80)
        print()

    # Sair
    elif option == '3':
        print('=' * 80)
        print('Sistema encerrado.')
        print('=' * 80)
        print()
        break

    # Condição para opção
    else:
        print('=' * 80)
        print('Opção inválida. Tente novamente.')
        print('=' * 80)
        print()
                
    # Pausa
    print('=' * 80)
    pause = input('Pressione Enter para continuar.\n')