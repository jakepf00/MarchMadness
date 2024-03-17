from Layer import Layer

# Inherit from the base class Layer
class ActivationLayer(Layer):
    def __init__(self, activation, activation_prime):
        self.activation = activation
        self.activation_prime = activation_prime

    # Returns the activated input
    def forward_propagation(self, input_data):
        self.input = input_data
        self.output = self.activation(self.input)
        return self.output
    
    # Returns input_error = dE/dX for a given output_error = dE/dY
    # learning_rate is not used because there is no "learnable" parameters
    def backwarg_propagation(self, output_error, learning_rate):
        return self.activation_prime(self.input) * output_error