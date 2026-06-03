import pandas as pd
from datetime import datetime
from models.queimada import Queimada
from algoritmos.busca import busca_uc
from estruturas.linked_list import LinkedList

def carregar_csv(caminho_arquivo):
    lista = LinkedList()
    try:
        df = pd.read_csv(caminho_arquivo, sep=";")
        for _, linha in df.iterrows():
            registro = Queimada(
                linha["UC"],
                linha["AREA"],
                linha["ANO"]
            )
            lista.insert_at_end(registro)
        return lista
    except Exception as erro:
        print(f"Erro ao carregar arquivo: {erro}")
        return None

def exportar_csv(lista, nomes_ucs):
    registros = []
    for uc in nomes_ucs:
        resultados = busca_uc(lista, uc)
        for registro in resultados:
            registros.append({
                "UC": registro.uc,
                "AREA": registro.area,
                "ANO": registro.ano
            })
    
    if not registros:
        print("Nenhum registro encontrado.")
        return
    
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    nome_arquivo = (f"exportacao_{timestamp}.csv")
    df = pd.DataFrame(registros)
    df.to_csv(nome_arquivo,sep=";",index=False)
    print(f"Arquivo gerado: {nome_arquivo}")