# ATIVIDADE 005 - ATIVIDADE L
# ALUNO: BRUNO C. RODGERS
# Data: 13/11/2024
# Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake). O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço.

import os


os.system('cls')

# Título
print('=' * 70)
print('LOGIN E SENHA PARA QUUEBRA DE LOOP')
print('=' * 70)
print()

# Criação do looping
while True:
    login = 'redbruno7'
    senha = 'lima_oscar_lima'

    print('=' * 70)
    login_usuario = input('Usuário: ')
    print('-' * 70)
    senha_usuario = input('Senha: ')

    # Validação de login
    if (login_usuario == login) and (senha_usuario == senha):
        print('-' * 70)
        print('Bem-vindo, Bruno!')
        print('=' * 70)
        break
    else:
        print('-' * 70)
        print('Usuário ou senha inválidos. Tente novamente.')
        print('=' * 70)
        print()
        continue
print()