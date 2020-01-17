from myinterface import ReaderInterface
import pandas as pd
import os

cwd = os.getcwd()


class ProcessSpreadSheet(ReaderInterface):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        # if self

    def read_all(self):
        # data = pd.read_csv(cwd + f"\\{self.filename}")
        return self.open()

    def read_first_two(self):
        first_two = pd.read_csv(cwd + f"\\{self.filename}", nrows=2)
        return first_two

    def read_last_two(self):
        # data = pd.read_csv(cwd + f"\\{self.filename}")
        return self.open().tail(2)

    def open(self):
        data = pd.read_csv(cwd + f"\\{self.filename}")
        return data

