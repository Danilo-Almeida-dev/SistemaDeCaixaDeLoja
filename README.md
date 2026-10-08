# 🛒 Sistema de Caixa de Loja

Sistema de caixa (PDV) para terminal, desenvolvido em Python puro. Simula o fluxo de uma venda em um mercado: consulta de produtos, montagem do carrinho, pagamento com cálculo de troco, baixa no estoque e registro no histórico de vendas, com os dados salvos em arquivos JSON.

Projeto criado para praticar lógica de programação, organização em módulos, manipulação de listas e dicionários, validação de entradas e persistência de dados.

## ✨ Funcionalidades

- **Listagem de produtos** com código, nome, preço e quantidade em estoque.
- **Carrinho de compras**
  - adiciona produtos pelo código;
  - soma a quantidade quando o mesmo produto é adicionado de novo;
  - impede adicionar mais unidades do que há em estoque, considerando o que já está no carrinho;
  - permite remover um item por completo ou só parte da quantidade.
- **Pagamento** em Dinheiro, Pix, Cartão de Crédito ou Cartão de Débito.
  - Em dinheiro, calcula o troco e recusa valores insuficientes.
  - Aceita valores com vírgula ou ponto (`10,50` ou `10.50`).
- **Controle de estoque**: o estoque só é atualizado depois que o pagamento é confirmado.
- **Histórico de vendas** com data/hora, itens, total, forma de pagamento, valor pago e troco.
- **Persistência em JSON**: estoque e histórico continuam salvos depois que o programa é fechado.
- **Validação de entradas**: textos no lugar de números, quantidades negativas ou zero, códigos inexistentes, opções de menu inválidas e arquivos JSON corrompidos são tratados sem encerrar o programa.

## 🛠️ Tecnologias

- **Python 3** (biblioteca padrão apenas, sem dependências externas)
  - `json`: leitura e gravação dos dados
  - `datetime`: data e hora das vendas
  - `os`: caminho dos arquivos de dados
  - `math`: validação de valores numéricos

## 📁 Estrutura do projeto

```
SistemaDeCaixaDeLoja/
├── main.py         # Ponto de entrada: menu principal e fluxo do sistema
├── produtos.py     # Catálogo/estoque: carregar, salvar e listar produtos
├── carrinho.py     # Adicionar, visualizar e remover itens do carrinho
├── vendas.py       # Finalização da venda, pagamento, troco e baixa no estoque
├── historico.py    # Criação, registro, persistência e exibição das vendas
└── README.md
```

Arquivos gerados automaticamente ao executar (ignorados pelo Git):

| Arquivo          | Conteúdo                                   |
|------------------|--------------------------------------------|
| `produtos.json`  | Estoque atual dos produtos                 |
| `historico.json` | Todas as vendas finalizadas                |

> Para restaurar o estoque inicial, basta apagar o `produtos.json`.

## ▶️ Como executar

Pré-requisito: [Python 3.8+](https://www.python.org/downloads/) instalado.

```bash
git clone https://github.com/Danilo-Almeida-dev/SistemaDeCaixaDeLoja.git
cd SistemaDeCaixaDeLoja
python main.py
```

## 💻 Exemplo de uso

```
================================
        SISTEMA DE CAIXA
================================

1 - Listar produtos
2 - Iniciar venda
3 - Visualizar carrinho
4 - Remover produto do carrinho
5 - Finalizar venda
6 - Histórico de vendas
7 - Sair
Escolha uma opção: 5
================================
        FINALIZANDO VENDA
================================
Produto: Feijão 1kg
Quantidade: 3
Subtotal: R$ 22.50
--------------------------------
Total da venda: R$ 22.50
================================
        PAGAMENTO
================================
Formas de pagamento disponíveis:
1 - Dinheiro
2 - Pix
3 - Cartão de Crédito
4 - Cartão de Débito
Escolha a forma de pagamento (1, 2, 3 ou 4): 1
Digite o valor pago em dinheiro: R$ 50
Pagamento realizado com sucesso! Troco: R$ 27.50
Venda finalizada com sucesso!
```

## 🧠 O que foi desenvolvido / aprendizados

- **Modularização**: cada arquivo tem uma responsabilidade (produtos, carrinho, vendas, histórico), e o `main.py` só coordena o menu.
- **Estruturas de dados**: produtos, itens do carrinho e vendas são representados com listas e dicionários.
- **Regras de negócio**:
  - o estoque disponível desconta o que já está no carrinho;
  - a baixa no estoque acontece só depois do pagamento aprovado;
  - a venda guarda uma cópia dos dados do produto (nome e preço daquele momento), para o histórico não mudar se o produto mudar depois.
- **Valores monetários**: o total e o troco são arredondados para centavos (`round(valor, 2)`), evitando erros de ponto flutuante como `0.1 + 0.2 = 0.30000000000000004`.
- **Tratamento de erros** com `try/except` (`ValueError`, `FileNotFoundError`, `json.JSONDecodeError`).
- **Persistência** com leitura e escrita de arquivos JSON em UTF-8.
- **Boas práticas**: `if __name__ == "__main__":` como ponto de entrada.

## 🚀 Possíveis melhorias futuras

- Cadastro, edição e exclusão de produtos pelo próprio menu.
- Exibir o subtotal e o total no "Visualizar carrinho".
- Usar `decimal.Decimal` para os cálculos monetários.
- Testes automatizados com `unittest` ou `pytest`.
- Relatório de vendas por dia e por forma de pagamento.

## 👤 Autor

**Danilo Almeida**: [GitHub](https://github.com/Danilo-Almeida-dev)
