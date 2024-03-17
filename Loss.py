import numpy as np

# Loss function and its derivative
def meanSquareError(yActual, yPredicted):
    return np.mean(np.power(yActual - yPredicted, 2))
def meanSquareErrorPrime(yActual, yPredicted):
    return 2*(yPredicted-yActual)/yActual.size