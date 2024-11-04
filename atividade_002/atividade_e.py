# AULA 06 - ATIVIDADE E
# Data: 30/10/2024
# A EMPRESA "TRAVELCALC" ESTÁ DESENVOLVENDO UM SISTEMA DE CÁLCULO DE PREÇOS DE PASSAGENS DE ÔNIBUS COM BASE NA DISTÂNCIA DA VIAGEM. 
# ELES PRECISAM DE UM PROGRAMA QUE SOLICITE AO USUÁRIO A DISTÂNCIA A DESEJADA E, EM SEGUIDA, CALCULE O PREÇO DA PASSAGEM DE ACORDO COM AS POLÍTICAS DA EMPRESA. 
# SEGUNDO ESSAS POLÍTICAS, VIAGENS DE ATÉ 200 KM TÊM UM CUSTO DE R$0,70 POR KM RODADO, ENQUANTO VIAGENS ACIMA DESSA DISTÂNCIA PASSAM A CUSTAR R$0,40 POR KM RODADO.

import os


os.system('cls')

# Título
print('=' * 70)
print('VALOR PASSAGEM DE ÔNIBUS - TRAVELCALC')
print('=' * 70)

# Entrada
distancia = float(input('Insira a distância a ser percorrida em KM: '))
resposta = ''

# Processamento
if (distancia <= 200):
    valor_1 = distancia * 0.70
    resposta = f'O valor total da passagem será de R${valor_1:.2f}.'
else:
    valor_2 = distancia * 0.40
    resposta = f'O valor total da passagem será de R${valor_2:.2f}.'
    
# Saída
print(resposta)
print('~' * 70)