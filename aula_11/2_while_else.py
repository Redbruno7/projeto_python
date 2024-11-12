# AULA 11 - COMANDO WHILE, ELSE
# Data: 12/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('ESTRUTURA DE CONTROLE - WHILE - ELSE')
print('=' * 70)
print()

# Contador
contador = 1

# Iteração entre 6 números
print('=' * 70)
print('Contagem de 6 números e finalização:')
print('=' * 70)
while contador < 7:
    print(f'Contador é: {contador}')
    contador += 1

# Iteração para saída maior que condição do while
else:
    print('-' * 70)
    print('While Finalizado!')
    print('=' * 70)
print()