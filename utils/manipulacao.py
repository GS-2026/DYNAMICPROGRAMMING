from models.queimada import Queimada
from algoritmos.busca import busca_uc

def adicionar_ocorrencia(lista):
    try:
        uc = str(input("Nome da UC(Unidade de Conservação) ou 0 para voltar: "))
        if uc == "0": return
        area = float(input("Área queimada (em hectares): ").replace(",", ".") )
        ano = int(input("Ano: "))

        nova_ocorrencia = Queimada(uc, area, ano)
        lista.insert_at_end(nova_ocorrencia)
        print("\nRegistro adicionado com sucesso.")
        print(f" - UC: {nova_ocorrencia.uc}")
        print(f" - Área: {nova_ocorrencia.area} ha")
        print(f" - Ano: {nova_ocorrencia.ano}")

    except ValueError:
        print("\nDados inválidos.")


def remover_ocorrencia(lista):
    uc = input("Digite a UC ou 0 para voltar: ")
    if uc == "0": return
    resultados = busca_uc(lista, uc)

    if not resultados:
        print("UC não encontrada.")
        return

    print("\n=== Registros Encontrados ===\n")
    for i, registro in enumerate(resultados, start=1):
        print(f"{i} - {registro}")

    if not resultados:
        print("\nNenhum registro encontrado.")
        return

    if len(resultados) == 1:
        escolha = 1
        registro_escolhido = resultados[0]
        lista.remove(registro_escolhido)
        print("\nRegistro removido com sucesso.")
        return

    try:
        escolha = int(input("\nEscolha o registro para remover: "))
        if escolha < 1 or escolha > len(resultados):
            print("Opção inválida.")
            return

        registro_escolhido = resultados[escolha - 1]
        lista.remove(registro_escolhido)
        print("Registro removido com sucesso.")

    except ValueError:
        print("Entrada inválida.")