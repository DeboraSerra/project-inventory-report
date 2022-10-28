from datetime import date


def validade_mais_proxima(list):
    year, month, day = list[0].split('-')
    validade = date(int(year), int(month), int(day))
    for data in list:
        year, month, day = data.split('-')
        transformed = date(int(year), int(month), int(day))
        if transformed < validade and transformed >= date.today():
            validade = transformed

    return validade


def fabricacao_mais_antiga(list):
    year, month, day = list[0].split('-')
    fabricacao = date(int(year), int(month), int(day))
    for data in list:
        year, month, day = data.split('-')
        transformed = date(int(year), int(month), int(day))
        if transformed < fabricacao:
            fabricacao = transformed

    return fabricacao


def empresa_com_mais_produtos(list):
    empresa = ''
    quant = 0
    for emp, qnt in list.items():
        if qnt >= quant and empresa is not None:
            quant = qnt
            empresa = emp
    return empresa

class SimpleReport:
    @staticmethod
    def generate(list):
        validades = [item['data_de_validade'] for item in list]
        fabricacoes = [item['data_de_fabricacao'] for item in list]
        empresa_qnt_produtos = {item['nome_da_empresa']: 0 for item in list}
        for item in list:
            empresa_qnt_produtos[item['nome_da_empresa']] += 1
        validade = validade_mais_proxima(validades)
        fabricacao = fabricacao_mais_antiga(fabricacoes)
        empresa = empresa_com_mais_produtos(empresa_qnt_produtos)
        return (
          f"Data de fabricação mais antiga: {str(fabricacao)}\n"
          f"Data de validade mais próxima: {str(validade)}\n"
          f"Empresa com mais produtos: {empresa}"
        )
