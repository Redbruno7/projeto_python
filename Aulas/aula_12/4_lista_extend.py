# AULA 12 - ESTRUTURA DE DADOS - LISTA / JUNÇÃO DE ELEMENTOS
# Data: 21/11/2024

import os


os.system('cls')

print('=' * 70)
print('LISTAS - FUNÇÃO EXTEND')
print('=' * 70)
print()

# Entrada listas
lista_1 = [100, 200]
pares = []

# Entrada usuário
print('=' * 70)
numeros = input('Digite números separados por espaço: ')
print('=' * 70)
print()

# Transformação em lista
lista_2 = numeros.split()

# Iteração números inseridos
for i in lista_2:
    
    # Casting inteiro
    inteiros = int(i)

    # Verificação de número par
    if inteiros % 2 == 0:

        # Inserção de valor par à lista pares
        pares.append(inteiros)

# Junção de elementos "Lista pares" à lista principal
lista_1.extend(pares)


# Saída
print('=' * 70)
print(f'Lista Par: {pares}')
print('-' * 70)
print(f'Lista Final: {lista_1}')
print('=' * 70)
print()