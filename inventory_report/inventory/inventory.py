import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def import_csv(path, type):
    with open(path) as file:
        raw_content = csv.DictReader(file)
        content = [item for item in raw_content]
        return content


def import_json(path, type):
    with open(path) as file:
        raw_content = json.load(file)
        content = [item for item in raw_content]
        return content


def import_xml(path, type):
    with open(path) as file:
        raw_content = file.read()
        content = [
            item for item in xmltodict.parse(raw_content)["dataset"]["record"]
        ]
        return content


class Inventory:
    @staticmethod
    def import_data(path, type):
        if ".csv" in path:
            content = import_csv(path, type)
        elif ".json" in path:
            content = import_json(path, type)
        else:
            content = import_xml(path, type)
        if type == "simples":
            report = SimpleReport.generate(content)
        elif type == "completo":
            report = CompleteReport.generate(content)
        else:
            raise TypeError
        return report
