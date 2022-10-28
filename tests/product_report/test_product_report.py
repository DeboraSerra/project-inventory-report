from datetime import datetime
from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 1
    nome_produto = "produto1"
    nome_empresa = "empresa1"
    fabricacao = datetime.today()
    validade = datetime(2024, 10, 28)
    n_de_serie = "PR1"
    armazenamento = "em geladeira"
    product = Product(
        id,
        nome_produto,
        nome_empresa,
        fabricacao,
        validade,
        n_de_serie,
        armazenamento,
    )
    expected1 = f"O produto {nome_produto} fabricado em {str(fabricacao)}"
    expected2 = f" por {nome_empresa} com validade até {str(validade)}"
    expected3 = f" precisa ser armazenado {armazenamento}."
    expected = expected1 + expected2 + expected3

    assert str(product) == expected
