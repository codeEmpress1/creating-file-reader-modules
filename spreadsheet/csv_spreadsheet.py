from reader import Reader
import pandas as pd
import os

cwd = os.getcwd()


class OpenSpreadSheet(Reader):
    def __init__(self, filename):
        self.filename = filename
        # self.mode = mode

    def read_all(self):
        data = pd.read_csv(cwd + f"\\{self.filename}")
        return data

    def read_first_two(self):
        first_two = pd.read_csv(cwd + f"\\{self.filename}", nrows=2)

        return first_two

    def read_last_two(self):
        return self.open().tail(2)

    def __next__(self):
        data = pd.read_csv(cwd + f"\\{self.filename}")
        for row in data:
            yield row
