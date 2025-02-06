# AULA 06 - OPERADORES RELACIONAIS
# Data: 29/10/2024

import os


os.system('cls')

# Título
print('=' * 70)
print('Estrutura Condicional: Operações Relacionais')
print('=' * 70)

# Entrada simples
a = 10
b = 5
c = 'José'
d = 'José'

# Igualdade (==)
if c == d:
    print(f'{c} é igual a {d}')
    print('~'*70)
else:
    print(f'{c} não é igual a {d}')

# Diferença (!=)
if a != c:
    print('~'*70)
    print(f'{a} é diferente de {c}')
    print('~'*70)
else:
    print(f'{a} não é diferente de {c}')

# Maior que (>)
if a    > b:
    print('~'*70)
    print(f'{a} é maior que {b}')
    print('~'*70)
else:
    print(f'{a} não é maior que {b}')

# Menor que (<)
if b < a:
    print('~'*70)
    print(f'{b} é menor que {a}')
    print('~'*70)
else:
    print(f'{b} não é menor que {a}')

# Maior ou igual a (>=)
if a >= b:
    print('~'*70)
    print(f'{a} é maior ou igual a {b}')
    print('~'*70)
else:
    print(f'{a} não é maior ou igual a {b}')

# Maior ou igual a (>=)
if b <= a:
    print('~'*70)
    print(f'{b} é menor ou igual a {a}')
    print('~'*70)
else:
    print(f'{b} não é menor ou igual a {a}')

print('Fim do programa!')
print('='*70)
print()
