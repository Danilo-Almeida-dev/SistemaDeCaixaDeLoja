import json
import os


ARQUIVO_PRODUTOS = os.path.join(os.path.dirname(__file__), "produtos.json")

# Estoque inicial, usado quando ainda não existe o arquivo produtos.json
PRODUTOS_PADRAO = [
    {
        "codigo": 1,
        "nome": "Açúcar 1kg",
        "preco": 10.0,
        "quantidade": 5
    },
    {
        "codigo": 2,
        "nome": "Arroz 5kg",
        "preco": 20.90,
        "quantidade": 10
    },
    {
        "codigo": 3,
        "nome": "Feijão 1kg",
        "preco": 7.50,
        "quantidade": 15
    },
    {
        "codigo": 4,
        "nome": "Macarrão 500g",
        "preco": 4.20,
        "quantidade": 8
    },
    {
        "codigo": 5,
        "nome": "Óleo de Soja 900ml",
        "preco": 6.80,
        "quantidade": 12
    }
]

produtos = []


def carregar_produtos():
    try:
        with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as arquivo:
            produtos.extend(json.load(arquivo))

    except FileNotFoundError:
        # Primeira execução: cria o arquivo com o estoque inicial
        produtos.extend(dict(produto) for produto in PRODUTOS_PADRAO)
        salvar_produtos()

    except json.JSONDecodeError:
        print(
            "Aviso: o arquivo de produtos está corrompido. "
            "Usando o estoque inicial."
        )
        produtos.extend(dict(produto) for produto in PRODUTOS_PADRAO)


def salvar_produtos():
    with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, ensure_ascii=False, indent=4)


def listar_produtos():
    print("================================")
    print("        LISTA DE PRODUTOS")
    print("================================")

    for produto in produtos:
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Quantidade em estoque: {produto['quantidade']}")
        print("--------------------------------")
