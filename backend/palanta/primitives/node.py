from abc import abstractmethod


class Node:
    def __init__(self):
        pass

    @abstractmethod
    def call(self, *args):
        pass

    def __call__(self, *args):
        # Todo verify args and results
        results = self.call(*args)
        return results
