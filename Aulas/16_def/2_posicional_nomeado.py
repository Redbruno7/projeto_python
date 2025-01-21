# AULA 16 - FUNÇÕES EM PYTHON - PARÂMENTROS OPCIONAL OU DEFAULT
# Data: 20/01/2024

import os


os.system('cls')

# Definir a função "def a(x = string, y = int, w = int, z = float):"
def dados_paciente(
    nome = 'Coly', nascimento = 2005, peso = 46, altura = 1.68):
    print('=' * 80)
    print(f'Bem-vindo(a) ao sistema Senac, {nome}!')
    print(f'O ano de nascimento da {nome} é {nascimento}.')
    print(f'O peso da {nome} é {peso} kg.')
    print(f'A altura da {nome} é {altura} m.')
    print('=' * 80)
    print()
    
# Invocar função "a()"
dados_paciente()
dados_paciente(nome='Isis', nascimento=1985, peso=46, altura=1.56)
dados_paciente(nascimento=2008, nome='Ágata', peso=46, altura=1.58)
dados_paciente(altura=1.66, peso=46, nome='Bia', nascimento=2008)