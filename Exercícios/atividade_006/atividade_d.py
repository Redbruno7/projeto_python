# ATIVIDADE 006 - ATIVIDADE D
# ALUNO: BRUNO C. RODGERS
# Data: 22/11/2024
# Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.

import os


os.system('cls')

# Título
print('=' * 80)
print('Média de Notas de Alunos')
print('=' * 80)
print()

# Entrada
lista_notas = []

# Flag
soma = 0

# Iteração 4 alunos
print('-' * 80)
for i in range(1, 5):
    nota = float(input(f'Digite a nota do {i}º aluno: '))
    print('-' * 80)

    # Inserção de valor na lista
    lista_notas.append(f'{nota:.2f}')

    # Soma
    soma += nota
print()

# Calculo média
media = soma / 4

# Saída
print('=' * 80)
print(f'Notas dos alunos respectivamente inseridas: {lista_notas}')
print('-' * 80)
print(f'A média dos alunos é: {media:.2f}')
print('=' * 80)