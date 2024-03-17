import numpy as np

from Network import Network
from FC_Layer import FCLayer
from ActivationLayer import ActivationLayer
from Activation import tanh, tanhPrime
from Loss import meanSquareError, meanSquareErrorPrime

# Training data
xTrain = np.array([[[0, 0]], [[0, 1]], [[1, 0]], [[1, 1]]])
yTrain = np.array([[[0]], [[1]], [[1]], [[0]]])

# Network
net = Network()
net.add(FCLayer(2, 3))
net.add(ActivationLayer(tanh, tanhPrime))
net.add(FCLayer(3, 1))
net.add(ActivationLayer(tanh, tanhPrime))

# Train
net.use(meanSquareError, meanSquareErrorPrime)
net.fit(xTrain, yTrain, epochs = 1000, learningRate = 0.1)

# Test
out = net.predict(xTrain)
print(out)