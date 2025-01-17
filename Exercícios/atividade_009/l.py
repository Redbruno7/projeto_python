# ATIVIDADE 009 - ATIVIDADE L
# ALUNO: BRUNO C. RODGERS
# Data: 14/01/2025
# Crie um programa para cadastrar filmes em um cinema. 
# Para cada filme, o programa deve armazenar informações como:
# º Título;
# º Gênero;
# º Duração;
# º Classificação indicativa.
# Usuário deve cadastrar 5 filmes.
# Opção para alterar informações.
# Filmes ordenados por título.
# Relatório de quantos filmes têm duração superior a 2 horas;
# E quantos têm classificação indicativa "Livre".


import os

# Limpar terminal
os.system('cls')

# Título
print('=' * 80)
print('DICIONÁRIO DE FILMES')
print('=' * 80)
print()

# Dict "dict = {}"
movies_dict = {}

# Lista "list = []"
movies_list = []

# Iterar usuário "for i in range(value)"
for i in range(5):
    print('=' * 80)
    title = input(f'Título do {i + 1}ª filme: ').strip().capitalize()
    print('-' * 80)
    gender = input(f'Gênero do filme: ').strip().capitalize()
    print('-' * 80)
    duration = int(input(f'Duração do filme em minutos: '))
    print('-' * 80)
    rating = input(f'Classificação indicativa: ').strip().capitalize()
    print('=' * 80)
    print()
    
    # Adicionar par key-value ao dict "dict[key] = value"
    movies_dict['Título'] = title
    movies_dict['Gênero'] = gender
    movies_dict['Duração'] = duration
    movies_dict['Classificação indicativa'] = rating
    
    # Adicionar uma cópia dos dicts à lista "list.append(dict.copy())"
    movies_list.append(movies_dict.copy())

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
    movies_sorted = sorted(movies_list, key = lambda movie: movie['Título'])
    
    # Iterar na lista "for i in list"
    print('=' * 80)
    for i in movies_sorted:
        
        # Iterar no dict "for key, value in i.items()"
        for key, value in i.items():
            print(f'{key}: {value}')
        print('=' * 80)
    print()
    
    # Menu
    print('=' * 80)
    print('Menu de opções:')
    print('-' * 80)
    print('1. Modificar informação de um filme.')
    print('-' * 80)
    print('2. Gerar relatório detalhado.')
    print('-' * 80)
    print('3. Sair.')
    print('-' * 80)
    option = input('Digite uma opção (1-3): ')
    print('=' * 80)
    print()
    
    # Modificar descrição do filme
    if option == '1':
        print('=' * 80)
        change = input(
            'Digite o título do filme para alterar suas informações: '
            ).strip().capitalize()
        print('=' * 80)
        print()
        
        # Iterar na lista "for i in list"
        for i in movies_sorted:
        
        # Condicionar existência "if i['key'] == a"
            if i['Título'] == change:
                print('=' * 80)
                print('Filme encontrado. Digite as novas informações '
                      'ou pressione Enter parar manter as atuais.')
                print('=' * 80)
                print()
                
                # Itera usuário
                print('=' * 80)
                new_title = input('Digite um novo título: '
                    ).strip().capitalize()
                    
                # Condicionar existência "if a"
                if new_title:
                    i['Título'] = new_title
                print('-' * 80)

                new_gender = input('Digite um novo gênero: '
                    ).strip().capitalize()
                
                if new_gender:
                    i['Gênero'] = gender
                print('-' * 80)

                new_duration = input(
                    'Digite uma nova duração em minutos: ').strip()
                
                if new_duration:
                        i['Duração'] = int(duration)

                print('-' * 80)
                new_rating = input(
                    'Digite uma nova classificação indicativa: '
                    ).strip().capitalize()
                
                if new_rating:
                        i['Classificação indicativa'] = rating
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
    elif option == '2':

        # Iterar na lista "for i in list"
        print('=' * 80)
        for i in movies_sorted:
        
        # Iterar no dict "for key, value in i.items()"
            for key, value in i.items():
                print(f'{key}: {value}')
            print('=' * 80)
        print()

        # Flag contador "a = 0"
        duration_count = 0

        # Iterar lista "for i in list"
        for i in movies_sorted:

            # Condicionar existência "if i['key'] > int"
            if i['Duração'] > 120:

                # Somar flag "a += 1"
                duration_count += 1
        
        # Flag contador safra "a = 0"
        rating_count = 0

        # Iterar lista "for i in list"
        for i in movies_sorted:

            # Condicionar existência "if i['key'] > int"
            if i['Classificação indicativa'] == 'Livre':

                # Somar flag "a += 1"
                rating_count += 1
                    
        # Saídas
        print('=' * 80)
        print(f'Quantidade de filmes com mais de 2 horas: {duration_count}')
        print('-' * 80)
        print(f'Quantidade de filmes com classificação indicativa livre: '
              f'{rating_count}')
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