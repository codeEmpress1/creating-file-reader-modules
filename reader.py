from abc import ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def read_first_two(self):
        pass

    @abstractmethod
    def read_last_two(self):
        pass