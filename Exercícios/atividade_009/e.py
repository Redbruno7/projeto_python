# ALUNO: BRUNO C. RODGERS
# Data: 22/01/2025
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
    name = input(f'Nome do {i + 1}º aluno: ').strip().capitalize()
    print('-' * 80)
    birth = int(input(f'Ano de nascimento: '))
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
    
    # Ordenar lista "x = sorted(list, key = lambda a: a['key'])"
    students_sorted = sorted(students_list, key = lambda student: student['Nome'])

    # Título
    print('=' * 80)
    print('Lista atual: ')
    print('=' * 80)
    print()    
    
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
            'Digite o nome do aluno para alterar seus dados: '
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
                new_name = input('Digite um novo nome: '
                    ).strip().capitalize()
                    
                # Condicionar existência "if a"
                if new_name:
                    i['Nome'] = new_name
                print('-' * 80)

                new_birth = input('Digite uma nova data de nascimento: '
                    ).strip().capitalize()
                
                if new_birth:
                    i['Data de nascimento'] = int(new_birth)
                print('-' * 80)

                new_register = input(
                    'Digite uma nova matrícula: ').strip()
                
                if new_register:
                        i['Matrícula'] = int(new_register)
                print('-' * 80)
                    
                print('Dados atualizadas com sucesso.')
                print('=' * 80)
                print()
                break
        else:
            print('=' * 80)
            print('Aluno não encontrado. Tente novamente.')
            print('=' * 80)
            print()

    # Buscar
    elif option == '2':
        print('=' * 80)
        find = int(input('Digite o número de matrícula do aluno: '))
        print('=' * 80)
        print()

        # Tornar falso "x = bool"
        found = False
        
        # Iterar na lista "for i in list:"
        for i in students_sorted:

            # Condicionar existência "if i['string'] == x:"
            if i['Matrícula'] == find:
                print('=' * 80)
                    
                # Tornar verdadeiro "x = bool"
                found = True
                    
                # Iterar no dict "for key, value in i.items():"
                for key, value in i.items():
                    print(f'{key}: {value}')
                print('=' * 80)
                print()
        
        # Condicionar existência "if not x:"     
        if not found:
            print('=' * 80)
            print('Aluno não encontrado.')
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

        # Contador "a = 0"
        birth_count = 0

        # Iterar lista "for i in list"
        for i in students_sorted:

            # Condicionar existência "if i['key'] > int"
            if i['Data de nascimento'] > 2000:

                # Somar contador "a += 1"
                birth_count += 1
        
        # Contador "a = 0"
        register_count = 0

        # Iterar lista "for i in list"
        for i in students_sorted:

            # Condicionar existência "if i['key'] == string"
            if i['Matrícula'] % 2 == 1:

                # Somar contador "a += 1"
                register_count += 1
                    
        # Saídas
        print('=' * 80)
        print(f'Quantidade de alunos que nasceram após o ano 2000: '
              f'{birth_count}')
        print('-' * 80)
        print(f'Quantidade de alunos com número de matrículas ímpares: '
              f'{register_count}')
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