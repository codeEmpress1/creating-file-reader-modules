from reader import Reader
from .file_manager import OpenFile


class ReadTextFile(Reader):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def read_all(self):
        all_data = list(line for line in self.open(self.filename, self.mode))
        return '\n'.join(all_data)

    def read_first_two(self):
        first_two = []
        i = 0;
        for line in self.open(self.filename, self.mode):
            if i < 2:
                first_two.append(line)
                i += 1
        return '\n'.join(first_two)

    def read_last_two(self):
        all_lines = self.open(self.filename, self.mode)
        return '\n'.join(list(all_lines)[-2:])

    def __next__(self):
        pass

    @staticmethod
    def open(filename, mode):
        with OpenFile(filename, mode) as file:
            for line in file:
                yield line

