def estatisticas_gerais(lista):
    atual = lista.head
    total_registros = 0
    soma_area = 0
    maior_area = 0
    maior_registro = None
    
    while atual:
        registro = atual.data
        total_registros += 1
        soma_area += registro.area
        if registro.area > maior_area:
            maior_area = registro.area
            maior_registro = registro
        atual = atual.next
    
    if total_registros == 0:
        print("Nenhum registro encontrado.")
        return
    
    media = soma_area / total_registros
    
    print("\n===== ESTATÍSTICAS =====")
    print(f"Total de registros: {total_registros}")
    print(f"Área total queimada: {soma_area:.2f} ha")
    print(f"Média por ocorrência: {media:.2f} ha")
    print(f"Maior ocorrência: {maior_registro}")