import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(
        path,
    ):
        if ".json" not in path:
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            raw_content = json.load(file)
            content = [item for item in raw_content]
            return content
