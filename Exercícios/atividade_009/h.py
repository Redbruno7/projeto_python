# ALUNO: BRUNO C. RODGERS
# Data: 22/01/2025
# Crie um dicionário ordenado por títuclo com entrada para 5 livros:
# º Título;
# º Autor;
# º Ano de publicação;
# º Número de páginas.
# Ações:
# - Alterar dados;
# Relatório:
# = Quantidade de livros com mais de 300 páginas;
# = Livros da autora J. K. Rowling.


import os

# Limpar terminal
os.system('cls')

# Título
print('=' * 80)
print('DICIONÁRIO DE LIVROS')
print('=' * 80)
print()

# Dict "dict = {}"
books_dict = {}

# Lista "list = []"
books_list = []

# Iterar usuário "for i in range(value)"
for i in range(5):
    print('=' * 80)
    title = input(f'Título do {i + 1}º livro: ').strip().capitalize()
    print('-' * 80)
    writer = input(f'Nome do autor(a): ').strip().capitalize()
    print('-' * 80)
    year = int(input(f'Ano de publicação: '))
    print('-' * 80)
    pages = int(input(f'Número de páginas: '))
    print('=' * 80)
    print()
    
    # Adicionar par key-value ao dict "dict[key] = value"
    books_dict['Título'] = title
    books_dict['Autor(a)'] = writer
    books_dict['Ano'] = year
    books_dict['Páginas'] = pages
    
    # Adicionar uma cópia dos dicts à lista "list.append(dict.copy())"
    books_list.append(books_dict.copy())

# Looping Menu "while True"
while True:
    
    # Limpar Terminal
    os.system('cls')
    
    # Ordenar lista "x = sorted(list, key = lambda a: a['key'])"
    books_sorted = sorted(books_list, key = lambda book: book['Título'])

    # Título
    print('=' * 80)
    print('Lista atual: ')
    print('=' * 80)
    print()    
    
    # Iterar na lista "for i in list"
    print('=' * 80)
    for i in books_sorted:
        
        # Iterar no dict "for key, value in i.items()"
        for key, value in i.items():
            print(f'{key}: {value}')
        print('=' * 80)
    print()
    
    # Menu
    print('=' * 80)
    print('Menu de opções:')
    print('-' * 80)
    print('1. Modificar dados de um livro.')
    print('-' * 80)
    print('2. Gerar relatório.')
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
            'Digite o título do livro para alterar seus dados: '
            ).strip().capitalize()
        print('=' * 80)
        print()
        
        # Iterar na lista "for i in list"
        for i in books_sorted:
        
        # Condicionar existência "if i['key'] == a"
            if i['Título'] == change:
                print('=' * 80)
                print('Livro encontrado. Digite os novos dados '
                      'ou pressione Enter parar manter os atuais.')
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

                new_writer = input('Digite um novo autor(a): '
                    ).strip().capitalize()
                
                if new_writer:
                    i['Autor(a)'] = new_writer
                print('-' * 80)

                new_year = input(
                    'Digite um novo ano de publicação: ').strip()
                
                if new_year:
                    i['Ano'] = int(new_year)
                print('-' * 80)
                
                new_pages = input('Digite um novo nº de páginas: ').strip()
                
                if new_pages:
                    i['Páginas'] = int(new_pages)
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

    # Relatório
    elif option == '2':

        # Iterar na lista "for i in list"
        print('=' * 80)
        for i in books_sorted:
        
        # Iterar no dict "for key, value in i.items()"
            for key, value in i.items():
                print(f'{key}: {value}')
            print('=' * 80)
        print()

        # Contador "a = 0"
        pages_count = 0

        # Iterar lista "for i in list"
        for i in books_sorted:

            # Condicionar existência "if i['key'] > int"
            if i['Páginas'] > 300:

                # Somar contador "a += 1"
                pages_count += 1
        
        # Contador "a = 0"
        writer_count = 0

        # Iterar lista "for i in list"
        for i in books_sorted:

            # Condicionar existência "if i['key'] == string"
            if i['Autor(a)'] == 'J. k. rowling':

                # Somar contador "a += 1"
                writer_count += 1
                    
        # Saídas
        print('=' * 80)
        print(f'Quantidade de livros com mais de 300 páginas: '
              f'{pages_count}')
        print('-' * 80)
        print(f'Quantidade de livros escritos por j. k. Rowling: '
              f'{writer_count}')
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