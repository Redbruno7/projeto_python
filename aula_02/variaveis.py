# AULA 02 - VARIÁVEIS
# Data: 22/10/2024

import os
os.system('cls')

print('-' * 70)
print('Estudo de variáveis')
print('=' * 70)

# Variáveis são declaradas por inferência
nome = 'Bruno C. Rodgers'
nascimento = 1999
altura = 1.78
peso = 67.3
carinhoso = True
complexo = 3j # Python trabalha diretamente com números complexos
PI = 3.14 # CONSTANTE, seu valor não deve ser alterado

# Saída utilizando o método type() para verificar o tipo da variável
print('\033[0m \033[31mTipos declarados:\033[0m')
print('A variável nome é do tipo: ', type(nome))
print('A variável nascimento é do tipo', type(nascimento))
print('A variável altura é do tipo', type(altura))
print('A variável peso é do tipo', type(peso))
print('A variável carinhoso é do tipo', type(carinhoso))
print('A variável complexo é do tipo', type(complexo))
print('A variável PI é do tipo', type(PI))
print('-' * 70)
print('')