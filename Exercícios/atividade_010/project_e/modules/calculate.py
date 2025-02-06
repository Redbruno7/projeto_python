def imc_calculate(data_list):
    height, weight = data_list
    imc = weight / (height ** 2)
    return imc

def classify(result):
    if result < 18.5:
        return 'Abaixo do peso ideal.'
    elif 18.5 <= result <= 24.9:
        return 'Peso ideal.'
    elif 25 <= result <= 29.9:
        return 'Acima do peso ideal.'
    elif 30 <= result <= 34.9:
        return 'Obesidade grau um.'
    elif 35 <= result <= 39.9:
        return 'Obesidade grau dois.'
    else:
        return'Obesidade grau três.'