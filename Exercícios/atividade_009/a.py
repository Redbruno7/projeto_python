# ATIVIDADE 009 - ATIVIDADE A
# ALUNO: BRUNO C. RODGERS
# Data: 14/01/2025
# Criar um dicionário com 4 elementos.
# Usuário deve inserir chaves e valores.
# Chaves únicas.
# Exibir dicionário ordenado pelas chaves.


import os


os.system('cls')

# Título
print('=' * 70)
print('CRIAR UM DICIONÁRIO COM 4 ELEMENTOS')
print('=' * 70)
print()

# Dict
dict_1 = {}

# Iterar 4 elementos "for i in range(value)"
for i in range(4):

    # Iterar chave
    while True:
        print('=' * 70)
        key = input(f'Digite a {i + 1}ª chave: ').strip().capitalize()
        print('-' * 70)

        # Condicionar chave "if key in dict"
        if key in dict_1:
            print('Erro. Insira uma chave única.')
            print('=' * 70)
            print()
        else:
            break

    # Iterar valor
    value = input(f'Digite o {i + 1}º valor: ').strip().capitalize()
    print('=' * 70)
    print()

    # Adicionar par chave-valor ao dict
    dict_1[key] = value

# Ordenação por chave
dict_ordenado = sorted(dict_1.items())

# Exibição
print('=' * 70)
for key, value in dict_ordenado:
    print(f'{key}: {value}')
print('=' * 70)
print()