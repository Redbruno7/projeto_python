import os


os.system('cls')

# Título
print('=' * 70)
print('Estrutura Condicional: Operações Lógicas')
print('=' * 70)

# Entrada
a = 10
b = 5
c = 'João'

# E (and) verdadeiro
print('E (and) VERDADEIRO')
if (a > 5 and b != c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
print('~' * 70)

# E (and) falso
print('E (and) FALSO')
if (a > 5 and b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
print('~' * 70)

# Ou (or) verdadeiro
print('OU (or) VERDADEIRO')
if (a > 5 or b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
print('~' * 70)

# Ou (or) falso
print('OU (or) FALSO')
if (a < 5 or c == 'Joana'):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
print('~' * 70)