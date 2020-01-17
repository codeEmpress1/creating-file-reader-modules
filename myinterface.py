from abc import ABC, abstractmethod


class ReaderInterface(ABC):
    @abstractmethod
    def read_all(self):
        pass

    def read_first_two(self):
        pass

    def read_last_two(self):
        pass