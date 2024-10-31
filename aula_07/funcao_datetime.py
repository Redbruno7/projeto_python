# AULA 07 - FUNÇÃO INTERNA - DATETIME
# Data: 31/10/2024

import os

# Importação das funções a serem utilizadas
from datetime import datetime
from datetime import date


os.system('cls')

# Entrada
data = datetime.now() # Variável para data
data_formatada = data.strftime('%d/%m/%Y') # Variável para data formatada
data_hora_formatado = data.strftime('%d/%m/%Y %H:%M') # Variável para data e hora formatada
# Receber o ano
data_atual = date.today()
nascimento = 1999
idade = data_atual.year - nascimento

# Saída
print(f'Data formatada: {data_formatada}')
print(f'Data e hora formatadas: {data_hora_formatado}')
print('-' * 70)
print(f'Data atual no sistema: {data_atual}')
print(f'Nascimento...........: {nascimento}')
print(f'Ano atual............: {data_atual.year}')
print(f'Sua idade é..........: {idade} anos.')
print('-' * 70)