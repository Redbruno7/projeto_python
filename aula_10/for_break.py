# AULA 10 - COMANDO FOR COM COMANDO BREAK
# Data: 12/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('ESTRUTURA DE CONTROLE - BREAK')
print('=' * 70)
print()

# Iteração entre 10 valores
print('=' * 70)
print('Iteração entre 10 números com interrupção:')
print('=' * 70)
for c in range(0, 10):
    print(f'Valor: {c}')

    # Condição para quebra de contagem
    if (c == 5):
        print('-' * 70)
        print(f'Contagem interropida no {c}')
        break

print('=' * 70)
print()