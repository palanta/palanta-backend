from abc import abstractmethod


class Node:
    def __init__(self):
        pass

    @abstractmethod
    def call(self, *args):
        pass

    def __call__(self, *args):
        results = self.call(*args)
