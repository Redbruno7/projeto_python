def create_lists():
    list_1 = ['Nome', 'Peso', 'Altura']
    list_2 = ['John', 40, 1.8]

    return list_1, list_2

def create_dict(list_1, list_2):
    return dict(zip(list_1, list_2))