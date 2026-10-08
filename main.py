from produtos import produtos, listar_produtos, carregar_produtos
from carrinho import iniciar_venda, visualizar_carrinho, remover_item_do_carrinho
from vendas import finalizar_venda
from historico import mostrar_historico_vendas, carregar_historico_vendas


def main():
    carregar_produtos()
    carregar_historico_vendas()

    print("================================")
    print("        SISTEMA DE CAIXA")
    print("================================")

    carrinho = []

    while True:
        print()
        print("1 - Listar produtos")
        print("2 - Iniciar venda")
        print("3 - Visualizar carrinho")
        print("4 - Remover produto do carrinho")
        print("5 - Finalizar venda")
        print("6 - Histórico de vendas")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_produtos()

        elif opcao == "2":
            iniciar_venda(produtos, carrinho)

        elif opcao == "3":
            visualizar_carrinho(carrinho)

        elif opcao == "4":
            remover_item_do_carrinho(carrinho)

        elif opcao == "5":
            finalizar_venda(carrinho)

        elif opcao == "6":
            mostrar_historico_vendas()

        elif opcao == "7":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print(
                "Opção inválida. "
                "Por favor, escolha uma opção válida."
            )


if __name__ == "__main__":
    main()
