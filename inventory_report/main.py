import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def main():
    args = sys.argv
    if len(args) < 3:
        print('Verifique os argumentos', file=sys.stderr)
        return
    _, path, type = args
    if '.json' in path:
        importer = JsonImporter
    elif '.csv' in path:
        importer = CsvImporter
    else:
        importer = XmlImporter
    importer_data = InventoryRefactor(importer)
    importer_data.import_data(path, type)
    list = importer_data.data
    if type == 'simples':
        reporter = SimpleReport
    else:
        reporter = CompleteReport
    print(reporter.generate(list), end='')
