# AULA 06 - ATIVIDADE G
# Data: 30/10/2024
# VOCÊ ESTÁ DESENVOLVENDO UM PROGRAMA PARA DETERMINAR SE TRÊS SEGMENTOS PODEM FORMAR UM TRIÂNGULO. 
# PARA ISSO, O PROGRAMA PRECISA RECEBER AS MEDIDAS DOS TRÊS SEGMENTOS E COMPARÁ-LAS ENTRE SI. 
# A RESPOSTA RESULTANTE DESSA COMPARAÇÃO DEVE INDICAR SE OS SEGMENTOS FORNECIDOS PODEM FORMAR UM TRIÂNGULO OU NÃO.
import os


os.system('cls')

# Título
print('=' * 70)
print('VERIFICAÇÃO DE FORMAÇÃO DE UM TRIÂNGULO')
print('=' * 70)

# Entrada
a = float(input('Insira um ano a ser verificado: '))
b = float(input('Insira um ano a ser verificado: '))
c = float(input('Insira um ano a ser verificado: '))
resposta = ''

# Processamento

if (a < b + c) and (b < a + c) and (c < a + b):
    resposta = f'As medidas dos segmentos informados formam um triângulo.'
else:
    resposta = f'Não é possível formar um triângulo com as medidas informadas.'
    
# Saída
print(resposta)
print('~' * 70)