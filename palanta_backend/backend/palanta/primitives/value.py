from .node import Node


class Value(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def call(self, *args):
        return self.value
