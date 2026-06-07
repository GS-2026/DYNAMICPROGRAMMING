def busca_uc(lista, nome_uc):
    atual = lista.head
    resultados = []
    while atual:
        try:
            if atual.data.uc.lower() == nome_uc.lower():
                resultados.append(atual.data)
        except (AttributeError, TypeError) as erro:
            print(f"Registro inválido ignorado: {erro}")
        atual = atual.next
    return resultados