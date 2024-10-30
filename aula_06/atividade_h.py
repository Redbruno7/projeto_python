# AULA 06 - ATIVIDADE H
# Data: 30/10/2024
# A EMPRESA "ROOTCALC" ESTÁ DESENVOLVENDO UM SOFTWARE DE CÁLCULO DE RAÍZES DE EQUAÇÕES QUADRÁTICAS PARA AUXILIAR ENGENHEIROS E CIENTISTAS EM SUAS ANÁLISES E PROJETOS. 
# ELES PRECISAM DE UM PROGRAMA QUE CALCULE AS RAÍZES DA EQUAÇÃO QUADRÁTICA 𝑥²−6𝑥+5 SEM DEPENDER DE FUNÇÕES OU MÉTODOS PREDEFINIDOS, 
# UTILIZANDO APENAS OS CONCEITOS E OPERAÇÕES BÁSICAS APRENDIDOS ATÉ O MOMENTO. 
# ESSAS RAÍZES SÃO CONHECIDAS COMO 𝑥’ = 5 E 𝑥’’ = 1, E O PROGRAMA DEVE SER CAPAZ DE CALCULAR ESSAS RAÍZES DE FORMA PRECISA, SEGUINDO OS PRINCÍPIOS MATEMÁTICOS FUNDAMENTAIS.
import os


os.system('cls')

# Título
print('=' * 70)
print('CÁLULO DAS RAÍZES DE EQUAÇÃO DE SEGUNDO GRAU - ROOTCALC')
print('=' * 70)

# Entrada
a = 1
b = -6
c = 5

# Processamento
delta = (b ** 2) - (4 * a * c)
raiz_delta = delta ** 0.5
raiz_1 = (- b + raiz_delta) / (2 * a)
raiz_2 = (- b - raiz_delta) / (2 * a)
   
# Saída
print(f'As raízes da equação proposta são: {raiz_1} e {raiz_2}.')
print('~' * 70)
print()