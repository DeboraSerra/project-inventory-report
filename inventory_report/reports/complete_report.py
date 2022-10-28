from datetime import date
from inventory_report.reports.simple_report import (
    SimpleReport,
    validade_mais_proxima,
    fabricacao_mais_antiga,
    empresa_com_mais_produtos,
)


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list):
        validades = [item["data_de_validade"] for item in list]
        fabricacoes = [item["data_de_fabricacao"] for item in list]
        empresa_qnt_produtos = {item["nome_da_empresa"]: 0 for item in list}
        for item in list:
            empresa_qnt_produtos[item["nome_da_empresa"]] += 1
        validade = validade_mais_proxima(validades)
        fabricacao = fabricacao_mais_antiga(fabricacoes)
        empresa = empresa_com_mais_produtos(empresa_qnt_produtos)
        for empresa, qnt in empresa_qnt_produtos.items():
            print(empresa, qnt)
        produtos_por_empresa = [
            f"- {empresa}: {qnt}\n"
            for empresa, qnt in empresa_qnt_produtos.items()
        ]
        print(produtos_por_empresa)
        return (
            f"Data de fabricação mais antiga: {str(fabricacao)}\n"
            f"Data de validade mais próxima: {str(validade)}\n"
            f"Empresa com mais produtos: {empresa}\n"
            f"Produtos estocados por empresa:\n".join(produtos_por_empresa)
        )
