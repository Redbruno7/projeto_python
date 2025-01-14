# ATIVIDADE 009 - ATIVIDADE A
# ALUNO: BRUNO C. RODGERS
# Data: 14/01/2025
# Faça um programa para criar um dicionário com pelo menos 4 elementos.
# O programa deve permitir que o usuário insira as chaves e valores.
# As chaves devem ser únicas, e o programa deve garantir isso.
# Após inserir todos os elementos, o programa deve exibir o dicionário ordenado pelas chaves.


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
    print('=' * 70)
    key = input(f'Digite a {i}ª chave: ').strip().capitalize()
    print('-' * 70)
    value = input(f'Digite o {i}º valor: ').strip().capitalize()
    print('=' * 70)
    