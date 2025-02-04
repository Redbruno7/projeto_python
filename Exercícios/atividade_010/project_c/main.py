# ALUNO: BRUNO C. RODGERS
# Data: 24/01/2025
# Crie uma função para verificar o registro de um aluno em um dicionário. 
# Imprimir registros do aluno. 
# Registros:
# º Nome;
# º Matrícula;
# º Data de nascimento.

import os


from modules.title import title
from modules.get_data import register_student

# Limpeza terminal
def clear_terminal():
    os.system('cls')

# Nav
cls_terminal = clear_terminal()
title()

# Software
student_list = []
student_list.append(register_student())

while True:
    print('=' * 80)
    continue_register = input('Deseja cadastrar outro aluno? (s/n): ').strip().lower()
    print('=' * 80)
    print()
    
    if continue_register == 's':
        student_list.append(register_student())

    elif continue_register == 'n':
        cls_terminal = clear_terminal()
        break
        
    else:
        print('=' * 80)
        print('Resposta inválida. Tente novamente.')
        print('=' * 80)
        print()
        
# Saída
print('=' * 80)
print('Alunos cadastrados:')
print('=' * 80)
print()

for i in student_list:
    print('=' * 80)
    for key, value in i.items():
        print(f'{key}: {value}')
    print('=' * 80)
    print()