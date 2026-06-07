from estruturas.fila import Fila
from estruturas.pilha import Pilha
from algoritmos.busca import busca_uc
from algoritmos.merge_sort import merge_sort
from utils.csv import carregar_csv, exportar_csv
from utils.conversor import linked_list_para_lista
from utils.estatisticas import estatisticas_gerais
from utils.grafico import gerar_grafico_comparativo, gerar_grafico_uc
from utils.manipulacao import (adicionar_ocorrencia, remover_ocorrencia)

lista = carregar_csv("dados/queimadas_UCs_federais.csv")

if lista is None:
    print("\nErro: não foi possível carregar o arquivo de dados. "
        "Coloque o arquivo 'queimadas_UCs_federais.csv' na pasta 'dados' e tente novamente.")
    print("ENCERRANDO O PROGRAMA...")
    exit(1)
historico = Pilha()
fila = Fila()

while True:
    print("\n===== MONITORAMENTO DE QUEIMADAS EM UNIDADES DE CONSERVAÇÃO =====")
    print("1 - Buscar Unidade de Conservação")
    print("2 - Exibir histórico de buscas")
    print("3 - Adicionar ocorrência manualmente")
    print("4 - Remover ocorrência")
    print("5 - Top 10 maiores áreas queimadas")
    print("6 - Estatísticas gerais")
    print("7 - Gerar gráfico temporal de uma UC")
    print("8 - Comparar múltiplas UCs")
    print("9 - Exportar UCs para CSV")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        while True:
            uc = input("\nDigite o nome da UC(Unidade de Conservação) ou 0 para voltar: ")
            if uc == "0":
                break
            
            resultados = busca_uc(lista, uc)
            historico.push(uc)
            
            if resultados:
                print(f"\n{len(resultados)} registros encontrados:\n")
                for registro in resultados:
                    print(registro)
            else:
                print("UC não encontrada.")

    elif opcao == "2":
        historico.display()

    elif opcao == "3":
        adicionar_ocorrencia(lista)

    elif opcao == "4":
        remover_ocorrencia(lista)

    elif opcao == "5":
        dados = linked_list_para_lista(lista)
        ordenados = merge_sort(dados)
        print("\n=== TOP 10 ÁREAS QUEIMADAS ===\n")
        for i, registro in enumerate(ordenados[:10], start=1):
            print(f"{i}º {registro}")

    elif opcao == "6":
        estatisticas_gerais(lista)

    elif opcao == "7":
        uc = input("\nDigite o nome da UC: ")
        resultados = busca_uc(lista, uc)
        if resultados:
            gerar_grafico_uc(lista, uc)
        else:
            print("UC não encontrada.")

    elif opcao == "8":
        nomes_ucs = []
        while True:
            uc = input("\nDigite o nome da UC (ou 0 para gerar o gráfico): ").strip()
            if uc == "0":
                break
            
            if any(nome.lower() == uc.lower() for nome in nomes_ucs):
                print("UC já adicionada.")
                continue
            
            resultados = busca_uc(lista, uc)
            
            if not resultados:
                print("UC não encontrada.")
                continue
            
            nomes_ucs.append(uc)
            
            print("UC adicionada com sucesso. "
                f"({len(resultados)} registros encontrados). ")
        
        if len(nomes_ucs) < 2:
            print("É necessário informar pelo menos duas UCs para comparação.\n")
        else:
            print("\nUCs selecionadas:")
            for i, uc in enumerate(nomes_ucs, start=1):
                print(f"{i}. {uc}")
            gerar_grafico_comparativo(lista,nomes_ucs)

    elif opcao == "9":
        enfileiradas = []
        
        while True:
            uc = input("\nDigite a UC ou 0 para processar exportações: ").strip()
            if uc == "0":
                break
            if any(nome.lower() == uc.lower() for nome in enfileiradas):
                print("UC já está na fila.")
                continue
            
            resultados = busca_uc(lista, uc)
            if not resultados:
                print("UC não encontrada.")
                continue
            fila.enqueue(uc)
            enfileiradas.append(uc)
            print(f"UC enfileirada ({len(resultados)} registros). "
                f"Total na fila: {fila.size()}")

        if fila.is_empty():
            print("Nenhuma UC na fila.")
        else:
            print(f"\nProcessando {fila.size()} exportação(ões)...")
            while not fila.is_empty():
                solicitacao = fila.dequeue()
                print(f"Exportando: {solicitacao}")
                exportar_csv(lista, [solicitacao])
            print("Todas as exportações concluídas.")

    elif opcao == "0":
        break