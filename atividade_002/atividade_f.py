# AULA 06 - ATIVIDADE F
# Data: 30/10/2024
# A EMPRESA "LEAPYEARCHECK" ESTÁ DESENVOLVENDO UM SOFTWARE DE VERIFICAÇÃO DE ANOS BISSEXTOS PARA AUXILIAR USUÁRIOS NA IDENTIFICAÇÃO DESSES ANOS DE FORMA RÁPIDA E PRECISA. 
# ELES PRECISAM DE UM PROGRAMA QUE PERMITA AOS USUÁRIOS INSERIR UM ANO E, EM SEGUIDA, DETERMINE SE ESSE ANO É BISSEXTO OU NÃO, 
# DE ACORDO COM AS REGRAS ESTABELECIDAS PELO CALENDÁRIO GREGORIANO. 
# ALÉM DISSO, É NECESSÁRIO REALIZAR A VALIDAÇÃO DE ENTRADA DE DADOS PARA GARANTIR QUE O ANO INSERIDO PELO USUÁRIO SEJA UM VALOR VÁLIDO, OU SEJA, UM NÚMERO INTEIRO POSITIVO.

import os


os.system('cls')

# Título
print('=' * 70)
print('VERIFICAÇÃO DE ANO BISSEXTO - LEAPYEARCHECK')
print('=' * 70)

# Entrada
ano = int(input('Insira um ano a ser verificado: '))
resposta = ''

# Processamento

if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    resposta = f'O ano {ano}, é bissexto.'
else:
    resposta = f'O ano {ano}, não é bissexto.'
    
# Saída
print(resposta)
print('~' * 70)