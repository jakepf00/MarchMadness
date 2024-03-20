import csv
import numpy as np
import pathlib

from Network import Network
from FC_Layer import FCLayer
from ActivationLayer import ActivationLayer
from Activation import tanh, tanhPrime
from Loss import meanSquareError, meanSquareErrorPrime

# Training data
pathlib.Path("TrainingData/").mkdir(parents=True, exist_ok=True)
trainingFileX = open("TrainingData/2024x.csv", "r")
trainingFileY = open("TrainingData/2024y.csv", "r")

xTrainList = []
yTrainList = []
xTrainCsv = csv.reader(trainingFileX, quoting=csv.QUOTE_NONNUMERIC)
yTrainCsv = csv.reader(trainingFileY, quoting=csv.QUOTE_NONNUMERIC)
for row in xTrainCsv:
    xTrainList.append([row])
for row in yTrainCsv:
    yTrainList.append([row])
xTrain = np.array(xTrainList)
yTrain = np.array(yTrainList)


# Network
net = Network()
net.add(FCLayer(4, 50))
net.add(ActivationLayer(tanh, tanhPrime))
net.add(FCLayer(50, 25))
net.add(ActivationLayer(tanh, tanhPrime))
net.add(FCLayer(25, 1))
net.add(ActivationLayer(tanh, tanhPrime))


# Train
net.use(meanSquareError, meanSquareErrorPrime)
net.fit(xTrain, yTrain, epochs = 10, learningRate = 0.1)


# Tests
pathlib.Path("MarchMadnessData/").mkdir(parents=True, exist_ok=True)
MarchMadnessFile = open("MarchMadnessData/2024.csv", "r")
MarchMadnessList = []
MarchMadnessCsv = csv.reader(MarchMadnessFile, quoting=csv.QUOTE_NONNUMERIC)
for row in MarchMadnessCsv:
    MarchMadnessList.append([row])
MarchMadness = np.array(MarchMadnessList)

out = net.predict(MarchMadness)
for prediction in out:
    print(prediction)