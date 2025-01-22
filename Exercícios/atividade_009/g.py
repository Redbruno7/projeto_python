# ALUNO: BRUNO C. RODGERS
# Data: 22/01/2025
# Crie um dicionário com as informações:
# º Nome: John;
# º Idade: 40;
# º Peso: 80;
# º Altura: 1.70.
# Ações:
# - Listar registros;
# - Alterar valores;
# - Excluir item específico;
# - Exibir apenas nome e altura.
# Exclusões somente se a chave existir.
# Listar o dicionário atualizado
# Relatório:
# = Quantidade de informações restantes;
# = Estado atual dos registros.


import os

# Limpar terminal
os.system('cls')

# Título
print('=' * 80)
print('DICIONÁRIO DO JOHN')
print('=' * 80)
print()

# Dict "dict = {}"
john_dict = {'Nome' : 'John', 'Idade': 40, 'Peso': 80, 'Altura': 1.70}

# Looping Menu "while True"
while True:
    
    # Limpar Terminal
    os.system('cls')

    # Título "print(str)"
    print('=' * 80)
    print('Dicionário atual: ')
    print('-' * 80)  
    
    # Iterar no dict "for key, value in i.items()"
    for key, value in john_dict.items():
        print(f'{key}: {value}')
    print('=' * 80)
    print()
    
    # Menu
    print('=' * 80)
    print('Menu de opções:')
    print('-' * 80)
    print('1. Modificar registro.')
    print('-' * 80)
    print('2. Excluir registro.')
    print('-' * 80)
    print('3. Exibir nome e altura.')
    print('-' * 80)
    print('4. Relatório.')
    print('-' * 80)
    print('5. Sair.')
    print('-' * 80)
    option = input('Digite uma opção (1-5): ')
    print('=' * 80)
    print()
    
    # Modificar descrição do filme
    if option == '1':
        print('=' * 80)
        change = input(
            'Digite a informação que deseja alterar: '
            ).strip().capitalize()
        print('=' * 80)
        print()
        
        # Tornar false "x = bool"
        found = False
        
        # Iterar no dict "for key, value in dict:"
        for key, value in john_dict.items():
            
            # Condicionar existência "if key == x"
            if key == change:
                        
                # Itera usuário "x = input(str)"
                print('=' * 80)
                new_data = input(f'Digite um novo valor para {change}: ')
                            
                # Condicionar existência "if x"
                if new_data:
                    
                    # Tornar verdadeiro "x = bool"
                    found = True
                    
                    # Alterar valor "dict[key] = x"
                    john_dict[key] = new_data
                    print('=' * 80)
                    print()
                    break
                
        if not found:
            print('=' * 80)
            print('Informação não encontrada. Tente novamente.')
            print('=' * 80)
            print()

    # Buscar
    elif option == '2':
        print('=' * 80)
        delete = input('Digite a informação que deseja excluir: '
                     ).strip().capitalize()
        print('=' * 80)
        print()

        # Tornar falso "x = bool"
        found = False

        # Iterar no dict "for key, value in dict.items():"
        for key, value in john_dict.items():
            
            # Condicionar existência "if key == x:"
            if key == delete:
                
                # Tornar verdadeiro "x = bool"
                found = True
                
                # Remover registro "del dict[key]"
                del john_dict[key]
                print('=' * 80)
                print('Registro excluído com sucesso.')
                print('=' * 80)
                print()
                break
        
        # Condicionar existência "if not x:"     
        if not found:
            print('=' * 80)
            print('Informação não encontrada.')
            print('=' * 80)
            print()
            
    # Exibir registros específicos
    elif option == '3':
        
        # Iterar no dict "for key, value in dict.items():"
        for key, value in john_dict.items():
            
            # Condicionar existência "if key == x:"
            if key == 'Nome':
                print('=' * 80)
                print(f'{key}: {value}')
                print('-' * 80)
            
            if key == 'Altura':
                print(f'{key}: {value}')
                print('=' * 80)
                print()

    # Relatório
    elif option == '4':
        
        # Iterar no dict "for key, value in i.items()"
        print('=' * 80)
        print('Dicionário atual:')
        print('-' * 80)
        for key, value in john_dict.items():
            print(f'{key}: {value}')
        print('=' * 80)
        print()

        # Contador "a = 0"
        register_count = 0

        # Iterar dict "for i in list"
        for i in john_dict:
            
            # Somar contador "x += int"
            register_count += 1

        # Saídas
        print('=' * 80)
        print(f'Quantidade de registros restantes: {register_count}')
        print('=' * 80)
        print()

    # Sair
    elif option == '5':
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