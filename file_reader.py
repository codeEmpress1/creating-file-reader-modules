from myinterface import ReaderInterface


class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


class ReadBytesFromFile(ReaderInterface):
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

    @staticmethod
    def open(filename, mode):
        with OpenFile(filename, mode) as file:
            for line in file:
                yield line

