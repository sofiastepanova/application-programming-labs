import csv


class ImageIterator:
    def __init__(self, path: str):
        self.path = path
        self.annotation = self.read(self.path)
        self.limit = len(self.annotation)
        self.counter = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.counter < self.limit:
            ne = self.annotation[self.counter]
            self.counter += 1
            return ne
        else:
            raise StopIteration


    def read(self, path: str) -> list:
        """
        :param path: Считывает CSV-файл
        :return: путь
        """
        with open(self.path, mode='r', encoding='utf-8') as scvf:
            reader = csv.reader(scvf)
            next(reader)
            return list(row[1] for row in reader)