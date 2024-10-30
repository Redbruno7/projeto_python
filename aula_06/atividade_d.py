# AULA 06 - ATIVIDADE D
# Data: 30/10/2024
# A EMPRESA "SALARYBOOST" ESTÁ IMPLEMENTANDO UM SISTEMA AUTOMATIZADO PARA CALCULAR OS AUMENTOS SALARIAIS DE SEUS FUNCIONÁRIOS COM BASE EM CRITÉRIOS ESPECÍFICOS. 
# ELES PRECISAM DE UM PROGRAMA QUE RECEBA COMO ENTRADA O SALÁRIO ATUAL DE UM FUNCIONÁRIO E, EM SEGUIDA, CALCULE O NOVO SALÁRIO COM BASE EM DETERMINADAS CONDIÇÕES. 
# ESSAS CONDIÇÕES INCLUEM UM AUMENTO DE 5% CASO O SALÁRIO ATUAL SEJA SUPERIOR A R$1500,00, E UM AUMENTO DE 10% CASO O SALÁRIO ATUAL SEJA INFERIOR A R$1000,00. 
# ALÉM DISSO, O PROGRAMA DEVE GARANTIR QUE O SALÁRIO INFORMADO NÃO SEJA IGUAL A ZERO OU NEGATIVO, POIS ISSO NÃO SERIA VÁLIDO.

import os


os.system('cls')

# Título
print('=' * 70)
print('CÁLCULO DE AUMENTO SALARIAL - SALARYBOOST')
print('=' * 70)

# Entrada
salario_atual = float(input('Insira o salário atual do funcionário: '))
resposta = ''


# Processamento
if (salario_atual <= 0):
    resposta = f'Valor inserido inválido!'
elif (salario_atual > 1500):
    reajuste_1 = salario_atual * 0.05
    resposta = f'O salário reajustado será de R${salario_atual + reajuste_1:.2f}'
elif (salario_atual <= 1500) and (salario_atual >= 1000):
    print(f'O salário de R${salario_atual:.2f} '
    'do funcionário se manterá o mesmo')
else:
    reajuste_2 = salario_atual * 0.1
    resposta = f'O salário reajustado será de R${salario_atual + reajuste_2:.2f}'

# Saída
print(resposta)
print('~' * 70)