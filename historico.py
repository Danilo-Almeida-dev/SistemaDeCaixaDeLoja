from datetime import datetime
import json
import os


ARQUIVO_HISTORICO = os.path.join(os.path.dirname(__file__), "historico.json")

historico_vendas = []


def carregar_historico_vendas():
    try:
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as arquivo:
            historico_vendas.extend(json.load(arquivo))

    except FileNotFoundError:
        pass

    except json.JSONDecodeError:
        print(
            "Aviso: o arquivo de histórico está corrompido. "
            "O histórico será iniciado vazio."
        )


def salvar_historico():
    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as arquivo:
        json.dump(historico_vendas, arquivo, ensure_ascii=False, indent=4)


def registrar_venda(venda):
    historico_vendas.append(venda)
    salvar_historico()


def criar_venda(carrinho, total, forma_pagamento, valor_pago=None, troco=None):
    data_hora = datetime.now()

    venda = {
        "data_hora": data_hora.strftime("%d/%m/%Y %H:%M:%S"),
        "itens": [],
        "total": total,
        "forma_pagamento": forma_pagamento,
        "valor_pago": valor_pago,
        "troco": troco
    }

    for item in carrinho:
        produto = item["produto"]

        item_venda = {
            "codigo": produto["codigo"],
            "nome": produto["nome"],
            "preco": produto["preco"],
            "quantidade": item["quantidade"]
        }

        venda["itens"].append(item_venda)

    return venda


def mostrar_historico_vendas():
    if not historico_vendas:
        print("Nenhuma venda registrada.")
        return

    print("================================")
    print("      HISTÓRICO DE VENDAS")
    print("================================")

    for venda in historico_vendas:
        print(f"Data e Hora: {venda['data_hora']}")
        print("Itens vendidos:")

        for item in venda["itens"]:
            print(f"  - Código: {item['codigo']}")
            print(f"    Nome: {item['nome']}")
            print(f"    Preço: R$ {item['preco']:.2f}")
            print(f"    Quantidade: {item['quantidade']}")
            print("--------------------------------")

        print(f"Total da venda: R$ {venda['total']:.2f}")
        print(f"Forma de pagamento: {venda['forma_pagamento']}")

        if venda["valor_pago"] is not None:
            print(f"Valor pago: R$ {venda['valor_pago']:.2f}")

        if venda["troco"] is not None:
            print(f"Troco: R$ {venda['troco']:.2f}")

        print("================================")
