# AULA 13 - ESTRUTURA DE DADOS - TUPLA
# Data: 29/11/2024

import os


os.system('cls')

print('=' * 70)
print('TUPLA - INTERAÇÃO COM USUÁRIO')
print('=' * 70)
print()

# Entrada
print('=' * 70)
numero_elementos = int(input('Quantos elementos na tupla? '))

# Lista
lista_elementos = []

# Iteração para obtenção dos elementos
for i in range(numero_elementos):
    while True:
        print('-' * 70)
        valor = input(f'Digite o {i + 1}º valor: ')


        # Condição número inteiro
        if valor.isdigit():
            lista_elementos.append(int(valor))
            break
        else:
            print('-' * 70)
            print('Entrada inválida. Digite um número inteiro.')
print('=' * 70)
print()

# Conversão tupla
tupla_elementos = tuple(lista_elementos)

# Saída tupla
print('=' * 70)
print(f'Tupla Criada: {tupla_elementos}')
print('=' * 70)
print()

# Iteração verificação de elemento indeterminada
print('=' * 70)
while True:
    valor = int(input('Verificar número na tupla: '))
    print('-' * 70)

    # Condição de presença
    if valor in tupla_elementos:
        print(f'O número {valor} está na tupla.')
        print('-' * 70)
    
        # Contagem de elementos
        contagem_elementos = tupla_elementos.count(valor)
        print(f'O número {valor} aparece {contagem_elementos} vez(es).')
        print('-' * 70)

        # Localização de primeira ocorrência
        indice = tupla_elementos.index(valor)
        print(f'A 1ª ocorrência de {valor} está no índice {indice}')
        print('=' * 70)
        print()
    else:
        print(f'O número {valor} não está na tupla.')
        print('=' * 70)
        print()

    # Repetição ou saída do laço
        print('=' * 70)
        continuar = input('Deseja continuar? (s/n): ').lower().strip()
        print('-' * 70)

        # Condição para quebra
        if continuar != 's':
            print(f'Encerrando o sistema...')
            print('=' * 70)
            print()
            break