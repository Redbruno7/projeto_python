# AULA 09 - UTILITÁRIOS (IN), (NOT IN)
# Data: 05/11/2024

import os


os.system('cls')

print('=' * 70)
print('UTILITÁRIOS "IN" E "NOT IN"')
print('=' * 70)

# Entrada
texto_1 = 'Olá, Mundo!'
texto_2 = 'Olá a todos!'
texto_3 = 'Olá, companheiros!'
texto_4 = 'Olá, a todo Mundo!'

# Verificar se palavra está contida na string
print(f'Frase analisada: "{texto_1}"')
print('.' * 70)
if "Mundo" in texto_1:
    print('A palavra "Mundo" está presente na string.')
    print('=' * 70)
else:
    print('A palavra "Mundo" não está presente na string.')
    print('=' * 70)
 
print(f'Frase analisada: "{texto_2}"')
print('.' * 70)
if "Mundo" in texto_2:
    print('A palavra "Mundo" está presente na string.')
    print('=' * 70)
else:
    print('A palavra "Mundo" não está presente na string.')
    print('=' * 70)
    
# Verificar se a palavra NÃO está contida na string
print(f'Frase analisada: "{texto_3}"')
print('.' * 70)
if "Mundo" not in texto_3:
    print('A palavra "Mundo" não está presente na string.')
    print('=' * 70)
else:
    print('A palavra "Mundo" está presente na string.')
    print('=' * 70)
 
print(f'Frase analisada: "{texto_4}"')
print('.' * 70)
if "Mundo" not in texto_4:
    print('A palavra "Mundo" não está presente na string.')
    print('=' * 70)
else:
    print('A palavra "Mundo" está presente na string.')
    print('=' * 70)