# ATIVIDADE 009 - ATIVIDADE C
# ALUNO: BRUNO C. RODGERS
# Data: 14/01/2025
# Crie um dicionário iterável com 5 ferramentas.
# Nome da ferramenta: chave, valor: descrição ou especificação técnica dessa ferramenta. 
# Opção de alterar valor de ferramenta já inserida.
# Imprimir valores de cada ferramenta.
# Imprimir a quantidade total de elementos presentes no dicionário. 
# Listar todas as ferramentas armazenadas e descrições, ordenadas alfabeticamente por nome. 
# Fornecer um relatório com a quantidade de ferramentas que têm mais de uma palavra no nome.


import os

# Limpar terminal
os.system('cls')

# Título
print('=' * 80)
print('DICIONÁRIO DE FERRAMENTAS')
print('=' * 80)
print()

# Dict "dict = {}"
tools_dict = {}

# Iterar 5 ferramentas "for i in range(value)"
for i in range(5):
    print('=' * 80)
    name = input(f'Nome da {i + 1}ª ferramenta: ').strip().capitalize()
    print('-' * 80)
    description = input(
        f'Descrição da {i + 1}ª ferramenta: ').strip().capitalize()
    print('=' * 80)
    print()
    
    # Adicionar par nome-descrição ao dict "dict[key] = value"
    tools_dict[name] = description

# Looping Menu "while True"
while True:
    
    # Limpar Terminal
    os.system('cls')
    
    # Ordenar dict pela chave "dict_2 = sorted(dict.items())"
    dict_ordem = sorted(tools_dict.items())
    
    # Exibir dict inicial ordenado "for key, value in dict.items()"
    print('=' * 80)
    print('Dicionário atual: ')
    print('-' * 80)
    for key, value in dict_ordem:
        print(f'{key}: {value}')
    print('=' * 80)
    print()
    
    # Menu
    print('=' * 80)
    print('Menu de opções:')
    print('-' * 80)
    print('1. Modificar descrição de uma ferramenta.')
    print('-' * 80)
    print('2. Exibir descrição de ferramenta específica.')
    print('-' * 80)
    print('3. Gerar relatório detalhado.')
    print('-' * 80)
    print('4. Sair.')
    print('-' * 80)
    option = input('Digite uma opção (1-4): ')
    print('=' * 80)
    print()
    
    # Modificar descrição da cor
    if option == '1':
        print('=' * 80)
        change = input(
            'Digite a ferramenta pra modificar sua descrição: '
            ).strip().capitalize()
        print('-' * 80)
        
        # Iterar usuário "value = input('')"
        if change in tools_dict:
            new_description = input(
                'Digite a nova descrição: ').strip().capitalize()
            print('-' * 80)
                
            # Atualizar descrição "dict[key] = value"
            tools_dict[change] = new_description
            print('Descrição atualizada.')
            print('=' * 80)
            print()
        else:
            print('Ferramenta não encontrada. Tente novamente.')
            print('=' * 80)
            print()
    
    # Exibir descrição específica
    elif option == '2':
        print('=' * 80)
        tool_description = input(
        'Digite a ferramenta para ver sua descrição: ').strip().capitalize()
        print('=' * 80)
        print()

        # Condição de existência "if a in dict"
        if tool_description in tools_dict:
            print('=' * 80)
            print(f'Descrição de {tool_description}: {tools_dict[key]}')
            print('=' * 80)
            print()
        else:
            print('=' * 80)
            print('Ferramenta não encontrada.')
            print('=' * 80)
            print()

    # Relatório
    elif option == '3':

        # Exibir dict inicial ordenado "for key, value in dict.items()"
        print('=' * 80)
        print('Dicionário atual: ')
        print('-' * 80)
        for key, value in dict_ordem:
            print(f'{key}: {value}')
        print('=' * 80)
        print()

        # Contar elementos "a = len(dict)"
        total_tools = len(tools_dict)
        print('=' * 80)
        print(f'Quantidade de elementos do dicionário: {total_tools}')
        print('=' * 80)
        print()

        # Identificar ferramentas com mais de uma palavra "a = [key for key in dict.keys if len(key.split()) > 1]"
        multi_tool_words = [
            key for key in tools_dict.keys() if len(key.split()) > 1]

        print('=' * 80)
        print(f'Quantidade de ferramentas com mais '
              f'de uma palavra no nome: {len(multi_tool_words)}.')
        print('=' * 80)
        print()

    # Sair
    elif option == '4':
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
    pause = input('Pressione Enter para continuar.')
    print('=' * 80)
    print()