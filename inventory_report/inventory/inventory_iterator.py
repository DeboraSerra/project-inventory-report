from typing import Iterator


class InventoryIterator(Iterator):
    def __init__(self, list) -> None:
        self.inventory = list
        self.__product_index = 0

    def __next__(self):
        try:
            product = self.inventory[self.__product_index]
        except IndexError:
            raise StopIteration()
        else:
            self.__product_index += 1
        return product
