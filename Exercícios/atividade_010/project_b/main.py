# ALUNO: BRUNO C. RODGERS
# Data: 04/02/2025
# Crie uma função para cadastrar:
# º Nome de um aluno(a);
# º Matrícula;
# º Data de nascimento.
# - Imprimir cadastros com loop for.

import os


from modules.title import title
from modules.get_data import register_student

# Limpar terminal
def clear_terminal():
    os.system('cls')

clear_terminal()
title()

# Registro aluno
student = register_student()

# Saída
print('=' * 80)
print('Informações do aluno:')
print('-' * 80)
for key, value in student.items():
    print(f'{key}: {value}')
print('=' * 80)
print()