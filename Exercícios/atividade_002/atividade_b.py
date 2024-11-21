# AULA 06 - ATIVIDADE B
# ALUNO: BRUNO C. RODGERS
# Data: 29/10/2024
# A EMPRESA "DATAMAX" ESTÁ DESENVOLVENDO UM NOVO SOFTWARE DE ANÁLISE ESTATÍSTICA E PRECISA DE UMA FUNCIONALIDADE QUE PERMITA AOS USUÁRIOS INSERIR TRÊS NÚMEROS E,
# EM SEGUIDA, EXIBIR NA TELA QUAL É O MAIOR NÚMERO, QUAL É O MENOR NÚMERO OU SE OS NÚMEROS SÃO TODOS IGUAIS.
# ESSA FUNCIONALIDADE É CRUCIAL PARA OS ANALISTAS DE DADOS DA "DATAMAX" QUE TRABALHAM COM CONJUNTOS DE DADOS DIVERSOS E PRECISAM RAPIDAMENTE IDENTIFICAR AS
# CARACTERÍSTICAS BÁSICAS DESSES CONJUNTOS, COMO A PRESENÇA DE OUTLIERS OU A UNIFORMIDADE DOS NÚMEROS.

import os


os.system('cls')

# Título
print('=' * 70)
print('ANÁLISE NUMÉRICA - DATAMAX')
print('=' * 70)

# Entrada
n1 = float(input('1º Valor: '))
n2 = float(input('2º Valor: '))
n3 = float(input('3º Valor: '))
resposta_1 = ''

# Processamento
if (n1 > n2) and (n1 > n3) and (n2 > n3):
    resposta = f'O maior número fornecido é: {n1}! E o menor é: {n3}!'
elif (n1 > n2) and (n1 > n3) and (n3 > n2):
    resposta = f'O maior número fornecido é: {n1}! E o menor é: {n2}!'
elif (n2 > n1) and (n2 > n3) and (n1 > n3):
    resposta = f'O maior número fornecido é: {n2}! E o menor é: {n3}!'
elif (n2 > n1) and (n2 > n3) and (n3 > n1):
    resposta = f'O maior número fornecido é: {n2}! E o menor é: {n1}!'
elif (n3 > n1) and (n3 > n2) and (n1 > n2):
    resposta = f'O maior número fornecido é: {n3}! E o menor é: {n2}!'
elif (n3 > n1) and (n3 > n2) and (n2 > n1):
    resposta = f'O maior número fornecido é: {n3}! E o menor é: {n1}!'
elif (n1 == n2) and (n1 > n3):
    resposta = f'O maior número fornecido é: {n1}! E o menor é: {n3}!'
elif (n1 == n2) and (n1 < n3):
    resposta = f'O maior número fornecido é: {n3}! E o menor é: {n1}!'
elif (n1 == n3) and (n1 > n2):
    resposta = f'O maior número fornecido é: {n1}! E o menor é: {n2}!' 
elif (n1 == n3) and (n1 < n2):
    resposta = f'O maior número fornecido é: {n2}! E o menor é: {n1}!'    
elif (n2 == n3) and (n1 > n2):
    resposta = f'O maior número fornecido é: {n1}! E o menor é: {n2}!'
elif (n2 == n3) and (n1 < n2):
    resposta = f'O maior número fornecido é: {n2}! E o menor é: {n1}!'
else:
    resposta = f'Todos os valores são iguais!'

# Saída
print(resposta)
print('~' * 70)