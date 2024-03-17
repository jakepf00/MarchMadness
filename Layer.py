# Base class
class Layer:
    def __init__(self):
        self.input = None
        self.output = None

    # Computes the output Y of a layer for a given input X
    def forwardPropagation(self, input):
        raise NotImplementedError

    # Computes dE/dX for a given dE/dY (and update parameters if any)
    def backwardPropagation(self, outputError, learningRate):
        raise NotImplementedError