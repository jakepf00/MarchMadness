import numpy as np

from Layer import Layer

# Inherit from base class Layer
class FCLayer(Layer):
    # input_size = number of input neurons
    # output_size = number of output neurons
    def __init__(self, inputSize, outputSize):
        self.weights = np.random.rand(inputSize, outputSize) - 0.5
        self.bias = np.random.rand(1, outputSize) - 0.5

    # Returns output for a given input
    def forwardPropagation(self, inputData):
        self.input = inputData
        self.output = np.dot(self.input, self.weights) + self.bias
        return self.output
    
    # Computes dE/dW, dE/dB for a given output_error = dE/dY. Returns input_error = dE/dX
    def backwardPropagation(self, outputError, learningRate):
        inputError = np.dot(outputError, self.weights.T)
        weightsError = np.dot(self.input.T, outputError)
        # dBias = output_error

        # Update parameters
        self.weights -= learningRate * weightsError
        self.bias -= learningRate * outputError
        return inputError