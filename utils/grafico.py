import os
from datetime import datetime
import matplotlib.pyplot as plt
from algoritmos.busca import busca_uc

agora = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

def gerar_grafico_uc(lista, nome_uc):
    resultados = busca_uc(lista, nome_uc)

    if not resultados:
        print("UC não encontrada.")
        return

    dados_por_ano = {}
    for registro in resultados:
        if registro.ano not in dados_por_ano:
            dados_por_ano[registro.ano] = 0
        dados_por_ano[registro.ano] += registro.area

    anos = sorted(dados_por_ano.keys())
    areas = [dados_por_ano[ano] for ano in anos]

    plt.figure(figsize=(10, 6))
    plt.plot(anos, areas, marker="o")
    plt.title(f"Área Queimada - {nome_uc}")
    plt.xlabel("Ano")
    plt.ylabel("Área Queimada (ha)")
    plt.grid(True)
    
    os.makedirs("graficos", exist_ok=True)
    nome_arquivo = (nome_uc.replace("/", "-").replace(" ", "_") + ".jpg")
    plt.savefig(f"graficos/{nome_arquivo}_{agora}.jpg")
    plt.close()
    print(f"Gráfico salvo em: graficos/{nome_arquivo}_{agora}.jpg")

def gerar_grafico_comparativo(lista, nomes_ucs):
    os.makedirs("graficos", exist_ok=True)
    plt.figure(figsize=(12, 6))

    for uc in nomes_ucs:
        dados_por_ano = {}
        atual = lista.head

        while atual:
            registro = atual.data
            if registro.uc.lower() == uc.lower():
                if registro.ano not in dados_por_ano:
                    dados_por_ano[registro.ano] = 0
                dados_por_ano[registro.ano] += registro.area
            atual = atual.next

        if not dados_por_ano:
            print(f"UC não encontrada: {uc}")
            continue

        anos = sorted(dados_por_ano.keys())
        areas = [dados_por_ano[ano] for ano in anos]

        plt.plot(anos, areas, marker="o", label=uc)

    plt.title("Comparação entre UCs")
    plt.xlabel("Ano")
    plt.ylabel("Área Queimada (ha)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"graficos/comparacao_ucs_{agora}.jpg")
    plt.close()
    print("Gráfico salvo em: " + f"graficos/comparacao_ucs_{agora}.jpg")