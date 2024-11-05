# ATIVIDADE 004 - ATIVIDADE A
# Data: 05/11/2024
# FAÇA UM PROGRAMA QUE SOLICITE SEPARADAMENTE O NOME, O NOME DO MEIO E O SOBRENOME DE UMA PESSOA. 
# EM SEGUIDA, IMPRIMA O NOME COMPLETO.

import os


os.system('cls')

print('=' * 70)
print('JUNÇÃO DE NOMES')
print('=' * 70)

# Entrada
primeiro_nome = input(f'Digite seu primeiro nome: ')
meio_nome = input(f'Digite seu nome do meio: ')
ultimo_nome = input(f'Digite seu sobrenome: ')

# Processamento
lista = [f'{primeiro_nome}', f'{meio_nome}', f'{ultimo_nome}']
juncao = ' '.join(lista)

# Saída
print(f'Olá, {juncao}, que nome potente!')
print(f'=' * 70)