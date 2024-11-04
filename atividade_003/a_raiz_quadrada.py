# ATIVIDADE 003 - ATIVIDADE A
# Data: 04/11/2024
# FAÇA UM PROGRAMA QUE RECEBA UM VALOR E MOSTRE SUA RAIZ QUADRADA. 
# PARA RAÍZES QUE NÃO SÃO EXATAS, ARREDONDE PARA CIMA OU PARA BAIXO. 
# FAÇA A VALIDAÇÃO PARA NÚMEROS NEGATIVOS, AVISANDO AO USUÁRIO QUE O RESULTADO SERÁ UM NÚMERO COMPLEXO.

import os
import math


os.system('cls')

print('=' * 70)
print('CÁLCULO DE RAIZ QUADRADA')
print('=' * 70)

# Entrada de dados
numero = float(input('Insira um valor: '))

# Processamento e Saída
if numero < 0:
    print('-' * 70)
    print(f'O resultado será um número complexo.')
else:
    raiz_quadrada = math.sqrt(numero)
    if raiz_quadrada.is_integer():
        print('-' * 70)
        print(f'A raiz quadrada de {numero} é: {raiz_quadrada:.0f}')
    else:
        arredondar_acima = math.ceil(raiz_quadrada)
        print('-' * 70)
        print(f'A raiz quadrada de {numero} '
            f'será aproximadamente: {arredondar_acima:.0f}')       
print('=' * 70)