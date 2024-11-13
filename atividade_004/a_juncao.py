# ATIVIDADE 004 - ATIVIDADE A
# ALUNO: BRUNO C. RODGERS
# Data: 05/11/2024

import os


os.system('cls')

print('=' * 70)
print('JUNÇÃO DE NOMES')
print('=' * 70)

# Entrada
print()
print('=' * 70)
primeiro_nome = input(f'Digite seu primeiro nome: ')
print('-' * 70)
meio_nome = input(f'Digite seu nome do meio: ')
print('-' * 70)
ultimo_nome = input(f'Digite seu sobrenome: ')
print('=' * 70)

# Processamento
lista = [f'{primeiro_nome}', f'{meio_nome}', f'{ultimo_nome}']
juncao = ' '.join(lista)

# Saída
print()
print('=' * 70)
print(f'Olá, {juncao}, que nome potente!')
print('=' * 70)