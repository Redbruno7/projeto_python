# Módulo para dividir 2 números

# Args>
    # a (Any): Dividendo
    # b (Any): Divisor

# Returns:
    # str: Mensagem de erro ou "Ok!" se a divisão for bem-sucedida
    # any: Quociente ou None em caso de erro

def dividir(a, b):
    if b == 0:
        return None, 'Erro de divisão'
    else:
        divisao = a / b
        return divisao, 'Ok!'