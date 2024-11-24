# ATIVIDADE 006 - ATIVIDADE G
# ALUNO: BRUNO C. RODGERS
# Data: 22/11/2024
# Ler uma lista com 10 números, depois apresente o maior e o menor número da lista

import os


os.system('cls')

# Título
print('=' * 70)
print('Leitura de Lista - Maior e menor Números')
print('=' * 70)
print()

# Entrada
lista = []

# Iteração 10 números
print('-' * 70)
for i in range (1, 11):
    numero = int(input(f'Digite o {i}º valor: '))
    print('-' * 70)

    # Inserção de valores
    lista.append(numero)
print()

# Ordenação e fatiamento menor número
lista.sort()
menor_numero = lista[0]
maior_numero = lista[-1]


# Saída
print('=' * 70)
print(f'Lista ordenada: {lista}')
print('-' * 70)
print(f'O menor número da lista é: {menor_numero}')
print('-' * 70)
print(f'O maior número da lista é: {maior_numero}')
print('=' * 70)
print()