# Trabalho sobre estrutura de dados SET
# Senac Minas Gerais / Juiz de Fora
# Aluno: Bruno C. Rodgers
# Turma: 0392
# Ano: 2024

# O programa executa o gerenciamento de um catálogo de jogos.
# Além de outras interações como vendas e comparação de inventários.

import os


os.system('cls')

# Título
print('=' * 140)
print('GERENCIAMENTO DE CATÁLOGO DE JOGOS - ALUGAMES')
print('=' * 140)
print()

# Catálogo inicial de jogos
catalogo = {'The Witcher 3', 'Cyberpunk 2077', 'Elden Ring', 
            'Dark Souls 3', 'God of War - Ragnarok', 'Fallout 4', 'Sekiro'}
promocao = {'The Witcher 3', 'Elden Ring', 'Sekiro'}
alugado = {'God of War - Ragnarok', 'Fallout 4'}
vendido = {'Cyberpunk 2077'}

# Saída Inicial
print('=' * 140)
print(f'Catálogo Inicial: {catalogo}')
print('-' * 140)
print(f'Jogos em Promoção: {promocao}')
print('-' * 140)
print(f'Jogos Alugados: {alugado}')
print('-' * 140)
print(f'Jogos Vendidos: {vendido}')
print('=' * 140)
print()
print('*' * 140)
print('MODIFICAÇÕES')
print('*' * 140)
print()

# 1 - Adicionar novo jogo ao catálogo
adicionar = 'Hollow Knight'
catalogo.add(adicionar)

# Saída 1
print('=' * 140)
print(f'1 - Jogo adicionado. Catálogo atualizado.')
print('-' * 140)
print(f'{catalogo}')
print('=' * 140)
print()

# 2 - Remover jogo do catálogo (após esgostar estoque)
remocao_1 = 'Dark Souls 3'
catalogo.remove(remocao_1)

# Saída 2
print('=' * 140)
print('2 - Jogo removido. Catálogo atualizado.')
print('-' * 140)
print(f'{catalogo}')
print('=' * 140)
print()

# 3 - Remover jogo de promoção com segurança de presença
remocao_2 = 'Sekiro'
promocao.discard(remocao_2)

# Saída 3
print('=' * 140)
print('3 - Jogo retirado de promoção. Catálogo de promoção atualizado.')
print('-' * 140)
print(f'{promocao}')
print('=' * 140)
print()

# 4 - Limpar lista de vendidos (zerar vendar de fim de mês)
vendido.clear()

# Saída 4
print('=' * 140)
print('4 - Lista de venda zerada. Catálogo de vendas atualizado.')
print('-' * 140)
print(f'{vendido}')
print('=' * 140)
print()

# 5 - Listar jogos indisponíveis (catálogo + promoção)
todos_jogos = catalogo.union(promocao)

# Saída 5
print('=' * 140)
print('5 - Lista de todos os jogos:')
print('-' * 140)
print(f'{todos_jogos}')
print('=' * 140)
print()

# 6 - Listar jogos indisponíveis
indisponivel = catalogo.intersection(alugado)

# Saída 6
print('=' * 140)
print('6 - Jogos indisponíveis:')
print('-' * 140)
print(f'{indisponivel}')
print('=' * 140)
print()

# 7 - Listar jogos que não estão em promoção
sem_promocao = catalogo.difference(promocao)

# Saída 7
print('=' * 140)
print('7 - Jogos que não estão em promoção:')
print('-' * 140)
print(f'{sem_promocao}')
print('=' * 140)
print()

# 8 - Listar jogos únicos (que estão em 1 grupo só)
jogos_unicos = alugado.symmetric_difference(vendido)

# Saída 8
print('=' * 140)
print('8 - Jogos alugados ou vendidos:')
print('-' * 140)
print(f'{jogos_unicos}')
print('=' * 140)
print()

# 9 - Verificar se jogos em promoção estão no catálogo
verificacao = promocao.issubset(catalogo)

# Saída 9
print('=' * 140)
print('9 - Os jogos em promoção estão listados no catálogo?')
print('-' * 140)
print(f'{verificacao}')
print('=' * 140)
print()