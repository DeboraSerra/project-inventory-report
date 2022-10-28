import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def import_csv(path, type):
    with open(path) as file:
      raw_content = csv.DictReader(file)
      content = [item for item in raw_content]
      if type == 'simples':
          report = SimpleReport.generate(content)
      elif type == 'completo':
          report = CompleteReport.generate(content)
      else:
          raise TypeError
      return report


def import_json(path, type):
    with open(path) as file:
      raw_content = json.load(file)
      content = [item for item in raw_content]
      if type == 'simples':
          report = SimpleReport.generate(content)
      elif type == 'completo':
          report = CompleteReport.generate(content)
      else:
          raise TypeError
      return report

class Inventory:
    @staticmethod
    def import_data(path, type):
        if '.csv' in path:
            return import_csv(path, type)
        elif '.json' in path:
            return import_json(path, type)
