import abc

class Parser:
    __metaclass__ = abc.ABCMeta

    def __init__(self, input_file_name):
        self.input_file = input_file_name

    @abc.abstractmethod
    def parse(self):
        return
