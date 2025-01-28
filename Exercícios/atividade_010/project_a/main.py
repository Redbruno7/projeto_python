# ALUNO: BRUNO C. RODGERS
# Data: 28/01/2025

import os

from modules.title import title
from modules.get_numbers import get_numbers

os.system('cls')

# Invocar funções
title()
even_list, odd_list, even_count, odd_count = get_numbers()


print('=' * 70)
print(f'Lista par: {even_list}')
print(f'Quantidade de elementos: {even_count}')
print('-' * 70)
print(f'Lista ímpar: {odd_list}')
print(f'Quantidade de elementos: {odd_count}')
print('=' * 70)
print()