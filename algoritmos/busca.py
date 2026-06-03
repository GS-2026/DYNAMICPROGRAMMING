def busca_uc(lista, nome_uc):
    atual = lista.head
    resultados = []
    while atual:
        if atual.data.uc.lower() == nome_uc.lower():
            resultados.append(atual.data)
        atual = atual.next
    return resultados