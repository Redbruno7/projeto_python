# ALUNO: BRUNO C. RODGERS
# Data: 30/01/2025
# Crie uma função para cadastrar:
# º Nome de um aluno(a);
# º Matrícula;
# º Data de nascimento.
# - Imprimir cadastros com loop for.

import os


from modules.title import title
from modules.get_datas import get_datas

# Limpar terminal
def clear_terminal():
    os.system('cls')

# Programa Principal
clear_terminal()
title()

# Entrada
print('=' * 80)
while True:
    name = input('Digite o nome do aluno: ').strip()
    print('-' * 80)

    if not name:
        print('Nome inválido. Tente novamente.')
        print('-' * 80)
    else:
        break

while True:
    register = input('Digite a matrícula do aluno: ')
    print('-' * 80)

    if not register.isdigit():
        print('Matrícula inválida. Tente novamente.')
        print('-' * 80)
    else:
        register = int(register)
        break

while True:
    birth = input('Digite a data de nascimento do aluno (dd/mm/aaaa): ')

    if not birth:
        print('-' * 80)
        print('Data de nascimento inválida. Tente novamente.')
        print('-' * 80)
    else:
        break
print('=' * 80)
print()

# Saída
data_dict = get_datas(nome = name, matricula = register, nascimento = birth)
print('=' * 80)
print('Informações do aluno:')
print('-' * 80)
for key, value in data_dict.items():
    print(f'{key}: {value}')
print('=' * 80)
print()