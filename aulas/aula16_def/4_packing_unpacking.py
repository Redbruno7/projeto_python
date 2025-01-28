# AULA 16 - FUNÇÕES EM PYTHON - PACK / UNPACKING
# Data: 28/01/2024

import os


os.system('cls')

# Título
print('=' * 80)
print('FUNÇÃO - PACK / UNPACKING')
print('=' * 80)
print()

# Definir função Pack
def packing(*list_num):
    print('=' * 80)
    print(f'Empacotados: {list_num}')
    print('-' * 80)
    for i in list_num:
        print(f'Empacotado: {i}')
    print('=' * 80)
    print()
        
# Invocar função Pack
packing(1, 2, 3, 4, 5)

# Definir função unpacking
def unpacking(a, b, c, d, e):
    print('=' * 80)
    print('Desempacotar:')
    print('-' * 80)
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print(f'd = {d}')
    print(f'e = {e}')
    print('=' * 80)
    print()
    
# Invocar função unpacking
list_numb = [1, 2, 3, 4, 5] # Lista
unpacking(*list_numb) # * args

# Definir função packing dicionário
def packing_dict(**data_dict): # ** Kwargs
    print('=' * 80)
    print(f'Dados do dicionário: {data_dict}')
    for key, value in data_dict.items():
        print('-' * 80)
        print(f'Chave: {key}')
        print(f'Valor: {value}')
    print('=' * 80)
    print()

# Invocar função packing dicionário
packing_dict(nome = 'Juquinha', idade = 70, peso = 70.5)

# Definir função unpacking dicionário
def unpacking_dict(nome, idade, peso):
    print('=' * 80)
    print(f'Nome = {nome}')
    print(f'Idade = {idade}')
    print(f'Peso = {peso}')
    print('=' * 80)
    print()

# Invocar função unpacking
data_dict = dict(nome = 'Maria', idade = 70, peso = 70.5)
unpacking_dict(**data_dict)