# ALUNO: BRUNO C. RODGERS
# Data: 06/02/2025
# º Criar uma função que receba 2 listas: 
# - lista 1: nome, peso, altura 
# - lista 2: John, 40, 1.8
# º Criar um dicionário utilizando como base as duas listas. 
# º Imprimir dicionário com laço for.

import os


from modules.print import title
from modules.create import create_lists, create_dict

# Limpeza de terminal
def cls_terminal():
    os.system('cls')

# Nav
cls_terminal()
title()

# Software
list_1, list_2 = create_lists()
john_dict = create_dict(list_1, list_2)

# Output
print('=' * 80)
for key, value in john_dict.items():    
    print(f'{key}: {value}')
print('=' * 80)
print()