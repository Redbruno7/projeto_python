# ATIVIDADE 007 - ATIVIDADE A
# ALUNO: BRUNO C. RODGERS
# Data: 22/11/2024
# Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair). 
# Após esta entrada de dados, faça o seguinte:
# Mostre a quantidade de notas que foram lidas.
# Exiba todas as notas na ordem em que foram informadas.
# Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# Calcule e mostre a soma das notas.
# Calcule e mostre a média das notas.


import os


os.system('cls')

# Título
print('=' * 70)
print('Leitura de Notas:')
print('=' * 70)
print()

# Entrada
lista_notas = []

# Flag
quantidade = 0

# Iteração notas
print('=' * 70)
print('Insira as notas. Digite "s" ou "0" para sair.')
print('-' * 70)
while True:
    nota = input('Digite uma nota: ').strip().lower()
    print('-' * 70)

    # Condição quebra de laço
    if nota == 's' or nota == '0':
        break
    
    # Inserção de valores na lista
    lista_notas.append(float(nota))

    # Contagem de notas inseridas
    quantidade += 1
print()

# Lista inversa conforme inserção
lista_inversa = lista_notas[::-1]

# Saída
print('=' * 70)
print(f'Quantidade de notas inseridas na lista: {quantidade}')
print('-' * 70)
print(f'Lista de notas respectivamente inseridas: {lista_notas}')
print('-' * 70)
print(f'Lista de notas inversa conforme inserção: {lista_inversa}')
print('-' * 70)

print('=' * 70)
print()