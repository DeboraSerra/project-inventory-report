from typing import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer) -> None:
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        content = self.importer.import_data(path)

        for item in content:
            self.data.append(item)

    def __iter__(self):
        return InventoryIterator(self.data)
