class Network:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.lossPrime = None

    # Add layer to network
    def add(self, layer):
        self.layers.append(layer)

    # Set loss to use
    def use(self, loss, lossPrime):
        self.loss = loss
        self.lossPrime = lossPrime

    # Predict output for given input
    def predict(self, inputData):
        # Sample dimension first
        samples = len(inputData)
        result = []

        # Run network over all samples
        for i in range(samples):
            # Forward propagation
            output = inputData[i]
            for layer in self.layers:
                output = layer.forwardPropagation(output)
            result.append(output)

        return result
    
    # Train the network
    def fit(self, xTrain, yTrain, epochs, learningRate):
        # Sample dimension first
        samples = len(xTrain)

        # Training loop
        for i in range(epochs):
            err = 0
            for j in range(samples):
                # Forward propagation
                output = xTrain[j]
                for layer in self.layers:
                    output = layer.forwardPropagation(output)

                # Compute loss (for display purpose only)
                err += self.loss(yTrain[j], output)

                # Backward propagation
                error = self.lossPrime(yTrain[j], output)
                for layer in reversed(self.layers):
                    error = layer.backwardPropagation(error, learningRate)
            
            # Calculate average error on all samples
            err /= samples
            print('epoch %d%d\terror=%f' % (i+1, epochs, err))