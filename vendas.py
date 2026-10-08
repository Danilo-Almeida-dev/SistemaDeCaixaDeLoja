import math

from historico import criar_venda, registrar_venda
from produtos import salvar_produtos


FORMAS_PAGAMENTO = {
    "1": "Dinheiro",
    "2": "Pix",
    "3": "Cartão de Crédito",
    "4": "Cartão de Débito"
}


def finalizar_venda(carrinho):
    print("================================")
    print("        FINALIZANDO VENDA")
    print("================================")

    if not carrinho:
        print(
            "O carrinho está vazio. "
            "Não há itens para finalizar a venda."
        )
        return

    total = 0.0

    for item in carrinho:
        produto = item["produto"]
        quantidade = item["quantidade"]

        subtotal = produto["preco"] * quantidade
        total += subtotal

        print(f"Produto: {produto['nome']}")
        print(f"Quantidade: {quantidade}")
        print(f"Subtotal: R$ {subtotal:.2f}")
        print("--------------------------------")

    # Arredonda para centavos, evitando erros de ponto flutuante
    total = round(total, 2)

    print(f"Total da venda: R$ {total:.2f}")

    print("================================")
    print("        PAGAMENTO")
    print("================================")

    print("Formas de pagamento disponíveis:")
    for codigo, nome in FORMAS_PAGAMENTO.items():
        print(f"{codigo} - {nome}")

    opcao_pagamento = input(
        "Escolha a forma de pagamento (1, 2, 3 ou 4): "
    ).strip()

    if opcao_pagamento not in FORMAS_PAGAMENTO:
        print(
            "Forma de pagamento inválida. "
            "A venda não pode ser finalizada."
        )
        return

    forma_pagamento = FORMAS_PAGAMENTO[opcao_pagamento]
    valor_pago = None
    troco = None

    if forma_pagamento == "Dinheiro":
        valor_digitado = input("Digite o valor pago em dinheiro: R$ ")

        try:
            # Aceita tanto "10.50" quanto "10,50"
            valor_pago = float(valor_digitado.replace(",", "."))

        except ValueError:
            print(
                "Valor inválido. "
                "Por favor, digite um número válido."
            )
            return

        if not math.isfinite(valor_pago) or valor_pago <= 0:
            print(
                "Valor inválido. "
                "Por favor, digite um número maior que zero."
            )
            return

        valor_pago = round(valor_pago, 2)

        if valor_pago < total:
            print(
                "Valor insuficiente. "
                "A venda não pode ser finalizada."
            )
            return

        troco = round(valor_pago - total, 2)
        print(f"Pagamento realizado com sucesso! Troco: R$ {troco:.2f}")

    else:
        print(f"Pagamento via {forma_pagamento} realizado com sucesso!")

    venda = criar_venda(carrinho, total, forma_pagamento, valor_pago, troco)
    registrar_venda(venda)

    # Atualiza o estoque somente após o pagamento
    for item in carrinho:
        produto = item["produto"]
        produto["quantidade"] -= item["quantidade"]

    salvar_produtos()
    carrinho.clear()

    print("Venda finalizada com sucesso!")
