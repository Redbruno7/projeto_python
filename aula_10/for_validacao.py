# AULA 10 - COMANDO FOR, RANGE COM VALIDAÇÃO E CASTING
# Data: 12/11/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('ESTRUTURA DE CONTROLE - VALIDAÇÃO E CASTING')
print('=' * 70)
print()

# Iteração entre 5 números
for c in range(0, 5):
    print('=' * 70)
    numero = input('Digite um número [0-5]: ')

    # Validação de número inteiro
    if (not (numero.isnumeric())):
        print('-' * 70)
        print(f'"{numero}" Entrada inválida!')
        print('=' * 70)
        print()
    else:
        numero = int(numero) # Casting da variável
        print('-' * 70)
    
        # Validação do intervalo (0 a 5)
        if (numero >= 0 and numero <= 5):
            print(f'O número {numero} está dentro do intervalo [0-5]!')
            print('=' * 70)
            print()
        else:
            print(f'"{numero}" Entrada inválida!')
            print('=' * 70)
            print()