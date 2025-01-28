# AULA 04 - EXERCÍCIO DE INTERPOLAÇÃO DE DADOS
# Data: 24/10/2024

# Import biblioteca sistema operacional
import os

# Import biblioteca de data e hora
import datetime

# Limpar terminal
os.system('cls')

# Título
print('~' * 70)
print('BEM-VINDO À GAMEWORLD')
print('~' * 70)

# Entrada de dados
nome = str(input('Entre com seu nome: '))
nome_jogo = str(input('Entre com o nome do jogo: '))
tempo_aluguel = int(input('Dia alugado: '))
valor = float(input('Valor total: '))

# Processamento: Pegar o ano corrente
dia_atual = datetime.datetime.now().day
aluguel =  int(dia_atual)- tempo_aluguel

# Saída interpolada
print('~' * 70)
print('INRFORMAÇÕES DE ALUGUEL')
print('~' * 70)
print(f'Olá, {nome}!')
print(f'Você alugou o jogo {nome_jogo} por {aluguel} dias')
print(f'O valor total é de: {valor}')
print('Esperamos que tenha se divertido!')