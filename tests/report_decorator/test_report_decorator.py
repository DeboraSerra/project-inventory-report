from datetime import datetime, timedelta
import pytest
from faker import Faker
from tests.factories.product_factory import ProductFactory
from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

faker = Faker("pt-BR")

old_date = faker.past_date()
future_date = faker.future_date() + timedelta(days=20)

oldest_date = old_date - timedelta(days=30)
closest_date = datetime.today().date() + timedelta(days=10)
company_bigger_stock = faker.company()


@pytest.fixture
def stock():
    return [
        vars(
            ProductFactory(
                data_de_fabricacao=str(old_date),
                data_de_validade=str(future_date),
            )
        ),
        vars(
            ProductFactory(
                nome_da_empresa=company_bigger_stock,
                data_de_fabricacao=str(old_date),
                data_de_validade=str(future_date),
            )
        ),
        vars(
            ProductFactory(
                nome_da_empresa=company_bigger_stock,
                data_de_fabricacao=str(old_date),
                data_de_validade=str(future_date),
            )
        ),
        vars(
            ProductFactory(
                data_de_fabricacao=str(oldest_date),
                data_de_validade=str(closest_date),
            )
        ),
    ]


def test_decorar_relatorio(stock):
    report = ColoredReport(SimpleReport).generate(stock)
    expected11 = "\033[32mData de fabricação mais antiga:\033[0m "
    expected12 = f"\033[36m{oldest_date}\033[0m\n"
    expected21 = "\033[32mData de validade mais próxima:\033[0m "
    expected22 = f"\033[36m{closest_date}\033[0m\n"
    expected31 = "\033[32mEmpresa com mais produtos:\033[0m "
    expected32 = f"\033[31m{company_bigger_stock}\033[0m"
    expected1 = expected11 + expected12
    expected2 = expected21 + expected22
    expected3 = expected31 + expected32
    expected = expected1 + expected2 + expected3
    assert report == expected
