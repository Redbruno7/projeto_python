# AULA 06 - ATIVIDADE C
# Data: 30/10/2024
# A EMPRESA "SAFEDRIVE" ESTÁ DESENVOLVENDO UM SISTEMA DE MONITORAMENTO DE VELOCIDADE PARA AJUDAR A PROMOVER A SEGURANÇA NAS ESTRADAS. 
# ELES PRECISAM DE UM PROGRAMA QUE PERMITA AOS USUÁRIOS INSERIR A VELOCIDADE DE UM CARRO E, EM SEGUIDA, EXIBIR NA TELA UMA MENSAGEM ADEQUADA COM BASE NA VELOCIDADE FORNECIDA. 
# O OBJETIVO PRINCIPAL É ALERTAR OS MOTORISTAS CASO ULTRAPASSEM O LIMITE DE VELOCIDADE DE 60 KM/H, INCENTIVANDO-OS A DIRIGIR DENTRO DOS LIMITES LEGAIS E,
# ASSIM, REDUZIR O RISCO DE ACIDENTES.

import os


os.system('cls')

# Título
print('=' * 70)
print('FISCALIZAÇÃO DE VELOCIDADE MÁXIMA- SAFEDRIVE')
print('=' * 70)

# Entrada
velocidade = float(input('Insira a velocidade em km/h: '))
resposta = ''

# Processamento
if (velocidade <= 60):
    resposta = f'A velocidade analisada de {velocidade:.0f} km/h, está dentro do limite máximo!'
else:
    resposta = f'A velocidade analisada de {velocidade:.0f} km/h, ultrapassa o limite máximo!'

# Saída
print(resposta)
print('~' * 70)