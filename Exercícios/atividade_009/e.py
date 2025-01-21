# ATIVIDADE 009 - ATIVIDADE E
# ALUNO: BRUNO C. RODGERS
# Data: 14/01/2025
# Cadastrar 5 alunos, com os dados: 
# º Nome.
# º Data de nascimento.
# º Número de matrícula.
# º Opção para alterar de dados já cadastrados. 
# º Exibir uma lista com alunos registrados com os dados de cada um. 
# º Gerar um relatório que informe:
    # - Quantos alunos nasceram após o ano de 2000.
    # - Quantos possuem números de matrícula ímpares. 
# Opção para buscar e exibir informações de um aluno específico a partir de seu número de matrícula.


import os

# Limpar terminal
os.system('cls')

# Título
print('=' * 80)
print('REGISTRO DE ALUNOS')
print('=' * 80)
print()

# Dict "dict = {}"
students_dict = {}

# Lista "list = []"
students_list = []

# Iterar usuário "for i in range(value)"
for i in range(5):
    print('=' * 80)
    name = input(f'Nome do {i + 1}ª aluno: ').strip().capitalize()
    print('-' * 80)
    birth = input(f'Data de nascimento: ').strip().capitalize()
    print('-' * 80)
    register = int(input(f'Número de matrícula: '))
    print('=' * 80)
    print()
    
    # Adicionar par key-value ao dict "dict[key] = value"
    students_dict['Nome'] = name
    students_dict['Data de nascimento'] = birth
    students_dict['Matrícula'] = register
    
    # Adicionar uma cópia dos dicts à lista "list.append(dict.copy())"
    students_list.append(students_dict.copy())

# Looping Menu "while True"
while True:
    
    # Limpar Terminal
    os.system('cls')
    
    # Exibir lista "for key, value in dict.items()"
    print('=' * 80)
    print('Lista atual: ')
    print('=' * 80)
    print()
    
    # Ordenar lista "x = sorted(list, key = lambda a: a['key'])"
    students_sorted = sorted(students_list, key = lambda student: student['Nome'])
    
    # Iterar na lista "for i in list"
    print('=' * 80)
    for i in students_sorted:
        
        # Iterar no dict "for key, value in i.items()"
        for key, value in i.items():
            print(f'{key}: {value}')
        print('=' * 80)
    print()
    
    # Menu
    print('=' * 80)
    print('Menu de opções:')
    print('-' * 80)
    print('1. Modificar dados de um aluno.')
    print('-' * 80)
    print('2. Procurar aluno.')
    print('-' * 80)
    print('3. Gerar relatório.')
    print('-' * 80)
    print('4. Sair.')
    print('-' * 80)
    option = input('Digite uma opção (1-4): ')
    print('=' * 80)
    print()
    
    # Modificar descrição do filme
    if option == '1':
        print('=' * 80)
        change = input(
            'Digite o Nome do aluno para alterar seus dados: '
            ).strip().capitalize()
        print('=' * 80)
        print()
        
        # Iterar na lista "for i in list"
        for i in students_sorted:
        
        # Condicionar existência "if i['key'] == a"
            if i['Nome'] == change:
                print('=' * 80)
                print('Aluno encontrado. Digite os novos dados '
                      'ou pressione Enter parar manter os atuais.')
                print('=' * 80)
                print()
                
                # Itera usuário
                print('=' * 80)
                new_name = input('Digite um novo Nome: '
                    ).strip().capitalize()
                    
                # Condicionar existência "if a"
                if new_name:
                    i['Nome'] = new_name
                print('-' * 80)

                new_birth = input('Digite uma nova Data de nascimento: '
                    ).strip().capitalize()
                
                if new_birth:
                    i['Data de nascimento'] = birth
                print('-' * 80)

                new_register = input(
                    'Digite uma nova matrícula em minutos: ').strip()
                
                if new_register:
                        i['Matrícula'] = int(register)
                print('-' * 80)
                    
                print('informações atualizadas com sucesso.')
                print('=' * 80)
                print()
                break
        else:
            print('=' * 80)
            print('Filme não encontrado. Tente novamente.')
            print('=' * 80)
            print()

    # Relatório
    elif option == '3':

        # Iterar na lista "for i in list"
        print('=' * 80)
        for i in students_sorted:
        
        # Iterar no dict "for key, value in i.items()"
            for key, value in i.items():
                print(f'{key}: {value}')
            print('=' * 80)
        print()

        # Flag contador "a = 0"
        register_count = 0

        # Iterar lista "for i in list"
        for i in students_sorted:

            # Condicionar existência "if i['key'] > int"
            if i['Matrícula'] > 120:

                # Somar flag "a += 1"
                register_count += 1
        
        # Flag contador safra "a = 0"
        rating_count = 0

        # Iterar lista "for i in list"
        for i in students_sorted:

            # Condicionar existência "if i['key'] == string"
            if i['Classificação indicativa'] == 'Livre':

                # Somar flag "a += 1"
                rating_count += 1
                    
        # Saídas
        print('=' * 80)
        print(f'Quantidade de filmes com mais de 2 horas: {register_count}')
        print('-' * 80)
        print(f'Quantidade de filmes com classificação indicativa livre: '
              f'{rating_count}')
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
    pause = input('Pressione Enter para continuar.\n')