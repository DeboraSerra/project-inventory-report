from datetime import datetime
from inventory_report.inventory.product import Product


def test_cria_produto():
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

    assert product.id == id
    assert product.nome_do_produto == nome_produto
    assert product.nome_da_empresa == nome_empresa
    assert product.data_de_fabricacao == str(fabricacao)
    assert product.data_de_validade == str(validade)
    assert product.numero_de_serie == n_de_serie
    assert product.instrucoes_de_armazenamento == armazenamento
