import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        with open(path) as file:
            raw_content = csv.DictReader(file)
            content = [item for item in raw_content]
            print(content)
            if type == 'simples':
                report = SimpleReport.generate(content)
            elif type == 'completo':
                report = CompleteReport.generate(content)
            else:
                raise TypeError
            return report
