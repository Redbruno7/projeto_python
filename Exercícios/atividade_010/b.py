# ALUNO: BRUNO C. RODGERS
# Data: 24/01/2025
# Crie uma função para cadastrar:
# º Nome de um aluno(a);
# º Matrícula;
# º Data de nascimento.
# - Imprimir cadastros com loop for.


import os

# Definir função "def function()"
def clear_terminal():
    os.system('cls')
            
def register_dict():

    # Criar dicionário cadastro "dict = {}"
    data_dict = {}
    
    # Criar loop nome "while bool:"
    print('=' * 80)
    while True:
        
        # Iterar usuário "a = input(str)"
        name = input('Digite o nome do aluno: ').strip()
        
        # Condicionar existência "if a:"
        if name:
            
            # Adicionar valor no dicionário "dict['key'] = value"
            data_dict['Nome'] = name
            
            # Quebrar loop "break"
            break
        
        # Fechar loop "else:"
        else:
            print('-' * 80)
            print('Nome inválido. Tente novamente.')
            print('-' * 80)

    # Criar loop matrícula
    print('=' * 80)
    while True:
        register = input('Digite o nº de matrícula do aluno: ').strip()

        if register.isdigit():
            data_dict['Matrícula'] = register
            break

        else:
            print('-' * 80)
            print('Número de matrícula inválido. Tente novamente.')
            print('-' * 80)

        
    # Criar loop data de nascimento
    print('=' * 80)
    while True:
        birth = input(
            'Digite a data de nascimento do aluno (dd/mm/aaaa): ').strip()
        
        if birth:
            data_dict['Data de nascimento'] = birth
            print('=' * 80)
            print()
            break
            
        else:
            print('-' * 80)
            print('Data de nascimento inválido. Tente novamente.')
            print('-' * 80)
        
    # Retornar resultado "return dict"
    return data_dict

# Programa Principal
print('=' * 80)
print('CADASTRO DE USUÁRIO')
print('=' * 80)
print()

# Chamar função "a = function()"
cls_terminal = clear_terminal()

# Chamar função em lista "data_list = [function()]"
data_list = [register_dict()]

# Iterar lista cadastro "for i in list:"
for i in data_list:
    
    # Iterar dicionário cadastro "for key, value in i.items():"
    print('=' * 80)
    for key, value in i.items():
        print(f'{key}: {value}')
    print('=' * 80)
    print()