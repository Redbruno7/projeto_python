# ATIVIDADE 003 - ATIVIDADE B
# ALUNO: BRUNO C. RODGERS
# Data: 04/11/2024
# FAÇA UM PROGRAMA QUE RECEBA 2 VALORES, FAÇA A DIVISÃO ENTRE ELES. 
# SE A DIVISÃO NÃO FOR INTEIRA, O PROGRAMA DEVERÁ ARREDONDAR O RESULTADO PARA CIMA E PARA BAIXO. 
# FAÇA A VALIDAÇÃO PARA DIVISÃO POR 0.

import os
import math


os.system('cls')

print('=' * 70)
print('DIVISÃO ARREDONDADA DE VALORES')
print('=' * 70)

# Entrada de dados
n1 = float(input('1º Valor: '))
n2 = float(input('2º Valor: '))

# Processamento e Saída
if n2 == 0:
    print('-' * 70)
    print(f'É impossível dividir qualquer número por 0.')
else:
    divisao = n1 / n2
    if divisao.is_integer():
        print('-' * 70)
        print(f'O número {n1} divido por {n2} é: {divisao:.0f}.')
    else:
        arredondar_acima = math.ceil(divisao)
        arredondar_abaixo = math.floor(divisao)
        print('-' * 70)
        print(f'O número {n1} dividido por {n2} estará entre os '
            f'inteiros: "{arredondar_abaixo:.0f}" e "{arredondar_acima}".')
print('=' * 70)