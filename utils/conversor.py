def linked_list_para_lista(linked_list):
    dados = []
    atual = linked_list.head

    while atual:
        dados.append(atual.data)
        atual = atual.next

    return dados