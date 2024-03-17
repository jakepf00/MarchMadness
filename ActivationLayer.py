from Layer import Layer

# Inherit from the base class Layer
class ActivationLayer(Layer):
    def __init__(self, activation, activationPrime):
        self.activation = activation
        self.activationPrime = activationPrime

    # Returns the activated input
    def forwardPropagation(self, inputData):
        self.input = inputData
        self.output = self.activation(self.input)
        return self.output
    
    # Returns input_error = dE/dX for a given output_error = dE/dY
    # learning_rate is not used because there is no "learnable" parameters
    def backwargPropagation(self, outputError, learningRate):
        return self.activationPrime(self.input) * outputError