import csv
import numpy as np
import pathlib

from Network import Network
from FC_Layer import FCLayer
from ActivationLayer import ActivationLayer
from Activation import tanh, tanhPrime
from Loss import meanSquareError, meanSquareErrorPrime

# Network parameters
numEpochs = 100
learningRate = 0.1
networkArchitecture = [4, 50, 25, 1] # First number must match number of input parameters, last must be 1 for output

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
for i in range(1, len(networkArchitecture)):
    net.add(FCLayer(networkArchitecture[i-1], networkArchitecture[i]))
    net.add(ActivationLayer(tanh, tanhPrime))


# Train
net.use(meanSquareError, meanSquareErrorPrime)
net.fit(xTrain, yTrain, epochs = numEpochs, learningRate = learningRate)


# March Madness Predictions
# Prepping March Madness data
pathlib.Path("MarchMadnessData/").mkdir(parents=True, exist_ok=True)
MarchMadnessFile = open("MarchMadnessData/2024.csv", "r")
MarchMadnessList = []
MarchMadnessCsv = csv.reader(MarchMadnessFile, quoting=csv.QUOTE_NONNUMERIC)
for row in MarchMadnessCsv:
    MarchMadnessList.append([row])
MarchMadness = np.array(MarchMadnessList)

# Making predictions
for n in range(1, 6):
    # Predict this round
    predictions = net.predict(MarchMadness)
    print("Round " + str(n) + ":")
    for prediction in predictions:
        print(prediction)

    # Prep next round
    nextRound = []
    for i in range(0, len(MarchMadness), 2):
        if predictions[i] > 0:
            match1 = np.array_split(MarchMadness[i][0], 2)[0]
        else:
            match1 = np.array_split(MarchMadness[i][0], 2)[1]

        if predictions[i+1] > 0:
            match2 = np.array_split(MarchMadness[i+1][0], 2)[0]
        else:
            match2 = np.array_split(MarchMadness[i+1][0], 2)[1]
        
        nextRound.append([np.concatenate([match1, match2])])
    MarchMadness = np.array(nextRound)

# Predict final round
predictions = net.predict(MarchMadness)
print("Round " + str(n) + ":")
for prediction in predictions:
    print(prediction)