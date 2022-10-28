from datetime import datetime
from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 1
    nome_produto = 'produto1'
    nome_empresa = 'empresa1'
    fabricacao = datetime.today()
    validade = datetime(2024, 10, 28)
    n_de_serie = 'PR1'
    armazenamento = 'em geladeira'
    product = Product(id, nome_produto, nome_empresa, fabricacao, validade, n_de_serie, armazenamento)
    expected = f'O produto {nome_produto} fabricado em {str(fabricacao)} por {nome_empresa} com validade até {str(validade)} precisa ser armazenado {armazenamento}.'

    assert str(product) == expected
