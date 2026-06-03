def merge_sort(registros):
    if len(registros) <= 1:
        return registros
    meio = len(registros) // 2
    esquerda = merge_sort(registros[:meio])
    direita = merge_sort(registros[meio:])
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []

    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i].area > direita[j].area:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado