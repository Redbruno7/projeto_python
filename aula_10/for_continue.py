# AULA 10 - COMANDO FOR COM COMANDO CONTINUE
# Data: 12/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('ESTRUTURA DE CONTROLE - FOR - CONTINUE')
print('=' * 70)
print()

# Iteração entre 10 números
print('=' * 70)
print('Iteração entre 10 números com pausa em determinado elemento')
print('=' * 70)
for c in range(1, 11):

    # Elemento fora do ciclo de iteração
    if c == 5:
        print('-' * 70)
        print(f'O elemento {c} pode ser trabalhado fora do loop.')
        print('-' * 70)
        continue

    # Saída dos números não trabalhados
    print(f'O número é {c}')

print('=' * 70)
print()