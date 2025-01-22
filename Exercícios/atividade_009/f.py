# ATIVIDADE 009 - ATIVIDADE F
# ALUNO: BRUNO C. RODGERS
# Data: 14/01/2025
# Dicionário com as informações:
# º Nome;
# º Idade;
# º Peso;
# º Altura 
# Inicializado com os valores: {'nome': 'John', 'idade': 40, 'peso': 80 e 'altura': 1.70}.
# Ações: 
# º Listar todas as chaves e respectivos valores do dicionário utilizando um laço de repetição. 
# º Excluir o peso. 
# º Listar chaves e valores restantes. 


import os

# Limpar terminal
os.system('cls')

# Título
print('=' * 80)
print('DICIONÁRIO DO JOHN')
print('=' * 80)
print()

# Dict "dict = {}"
john_dict = {'Nome' : 'John', 'Idade': 40, 'Peso': 80, 'Altura': 1.70}

# Título "print(str)"
print('=' * 80)
print('Dicionário inicial:')
print('-' * 80)
    
# Iterar no dict "for key, value in i.items()"
for key, value in john_dict.items():
    print(f'{key}: {value}')
print('=' * 80)
print()

# Excluir registro "del x[key]"
del john_dict['Peso']

# Iterar no dict "for key, value in i.items()"
print('=' * 80)
print('Dicionário final:')
print('-' * 80)
for key, value in john_dict.items():
    print(f'{key}: {value}')
print('=' * 80)
print()