import numpy as np
from .node import Node


class Add(Node):
    def call(self, *args):
        return sum(args)


class Subtract(Node):
    def call(self, *args):
        return args[0] - args[1]


class Multiply(Node):
    def call(self, *args):
        return np.prod(args)


class Divide(Node):
    def call(self, *args):
        return args[0] / args[1]
