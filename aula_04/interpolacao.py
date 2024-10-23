# AULA 04 - INTERPOLAÇÃO DE DADOS
# Data: 23/10/2024

# Import biblioteca sistema operacional
import os

# Import biblioteca de data e hora
import datetime

# Limpar terminal
os.system('cls')

# Título
print('-' * 70)
print('ENTRADA DE DADOS EM PYTHON')
print('=' * 70)

# Entrada de dados
nome = input('Entre com um nome: ')
peso = input('Entre com o peso: ')
altura = input('Entre com a altura: ')

# Entrada com casting
nascimento = int(input('Ano de nascimento: '))
cep = str(input('Entre com o CEP: '))
bairro = str(input('Nome do bairro: '))
rua = str(input('Nome da rua: '))
numero = int(input('Número: '))

# Processamento: Pegar o ano corrente
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento

# Saída simples
print('-' * 70)
print('SAÍDA DE DADOS')
print('=' * 70)
print('Nome..............: ', nome)
print('Data de nascimento: ', nascimento)
print('Peso..............: ', peso)
print('Altura............: ', altura)

# Saída interpolada
print(f'{nome}, você tem {idade} anos!')
print(f'CEP..............: {cep}')
print(f'Bairro...........: {bairro}')
print(f'Rua..............: {rua}')
print(f'Número...........: {numero}')
print('')