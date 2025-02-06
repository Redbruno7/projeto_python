import operator

def perform_operate(list_num, option, numb_operator):
    op_1, op_2 = list_num

    operate = {
        1: operator.add,
        2: operator.sub,
        3: operator.mul,
        4: operator.truediv,
        5: operator.floordiv,
        6: operator.mod
    }

    symbol = {
        1: '+',
        2: '-',
        3: '*',
        4: '/',
        5: '//',
        6: '%'
    }

    if option in operate and option in symbol:
        result_1 = f'{op_1} {symbol[option]} {numb_operator} = {
            operate[option](op_1, numb_operator)}'
        result_2 = f'{op_2} {symbol[option]} {numb_operator} = {
            operate[option](op_2, numb_operator)}'
        return result_1, result_2