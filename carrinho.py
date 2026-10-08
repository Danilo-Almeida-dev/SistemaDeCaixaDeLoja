def iniciar_venda(produtos, carrinho):
    print("================================")
    print("        INICIANDO VENDA")
    print("================================")

    while True:
        codigo_produto = input(
            "Digite o código do produto "
            "(ou 'sair' para encerrar a venda): "
        ).strip()

        if codigo_produto.lower() == "sair":
            break

        produto_encontrado = None

        for produto in produtos:
            if str(produto["codigo"]) == codigo_produto:
                produto_encontrado = produto
                break

        if produto_encontrado:

            try:
                quantidade = int(input(
                    f"Digite a quantidade de "
                    f"{produto_encontrado['nome']} "
                    f"que deseja adicionar ao carrinho: "
                ))

            except ValueError:
                print(
                    "Quantidade inválida. "
                    "Por favor, digite um número inteiro."
                )
                continue

            if quantidade <= 0:
                print(
                    "Quantidade inválida. "
                    "Digite um número inteiro positivo."
                )
                continue

            quantidade_no_carrinho = 0
            item_existente = None

            for item in carrinho:
                if item["produto"]["codigo"] == produto_encontrado["codigo"]:
                    quantidade_no_carrinho += item["quantidade"]
                    item_existente = item
                    break

            quantidade_disponivel = (
                produto_encontrado["quantidade"]
                - quantidade_no_carrinho
            )

            if quantidade <= quantidade_disponivel:

                if item_existente:
                    item_existente["quantidade"] += quantidade

                else:
                    carrinho.append({
                        "produto": produto_encontrado,
                        "quantidade": quantidade
                    })

                print(
                    f"{quantidade} unidade(s) de "
                    f"{produto_encontrado['nome']} "
                    f"adicionada(s) ao carrinho."
                )

            else:
                print(
                    f"Quantidade indisponível. "
                    f"Quantidade disponível: {quantidade_disponivel}"
                )

        else:
            print(
                "Produto não encontrado. "
                "Por favor, verifique o código e tente novamente."
            )


def visualizar_carrinho(carrinho):
    print("================================")
    print("        CARRINHO DE COMPRAS")
    print("================================")

    if not carrinho:
        print("O carrinho está vazio.")

    else:
        for item in carrinho:
            produto = item["produto"]
            quantidade = item["quantidade"]

            print(f"Produto: {produto['nome']}")
            print(f"Quantidade: {quantidade}")
            print(f"Preço unitário: R$ {produto['preco']:.2f}")
            print("--------------------------------")


def remover_item_do_carrinho(carrinho):
    print("================================")
    print("        REMOVER ITEM DO CARRINHO")
    print("================================")

    if not carrinho:
        print("O carrinho está vazio. Não há itens para remover.")
        return

    for item in carrinho:
        produto = item["produto"]
        quantidade = item["quantidade"]

        print(f"Código: {produto['codigo']}")
        print(f"Produto: {produto['nome']}")
        print(f"Quantidade: {quantidade}")
        print("--------------------------------")

    codigo_produto = input(
        "Digite o código do produto que deseja remover "
        "(ou 'sair' para cancelar): "
    ).strip()

    if codigo_produto.lower() == "sair":
        return

    item_removido = None

    for item in carrinho:
        if str(item["produto"]["codigo"]) == codigo_produto:
            item_removido = item
            break

    if item_removido:

        quantidade_remover = input(
            f"Digite a quantidade de "
            f"{item_removido['produto']['nome']} que deseja remover: "
        )

        try:
            quantidade_remover = int(quantidade_remover)
        except ValueError:
            print(
                "Quantidade inválida. "
                "Por favor, digite um número inteiro."
            )
            return

        if quantidade_remover <= 0:
            print(
                "Quantidade inválida. "
                "Por favor, digite um número maior que zero."
            )
            return

        if quantidade_remover > item_removido["quantidade"]:
            print(
                f"Quantidade solicitada excede o disponível no carrinho. "
                f"Quantidade disponível: {item_removido['quantidade']}"
            )
            return

        if quantidade_remover == item_removido["quantidade"]:
            carrinho.remove(item_removido)

        else:
            item_removido["quantidade"] -= quantidade_remover

        print(
            f"{quantidade_remover} unidade(s) de "
            f"{item_removido['produto']['nome']} "
            f"removida(s) do carrinho."
        )

    else:
        print(
            "Produto não encontrado no carrinho. "
            "Por favor, verifique o código e tente novamente."
        )
