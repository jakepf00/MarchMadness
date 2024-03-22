# March Madness AI Bracket Generator

Neural network built to predict the winners of March Madness NCAA Basketball games.

## Features

Implemented features include:
- Web scraper to collect team statistics
- Web scraper to collect game data from regular season
- Neural network built from scratch

All features are built using Python.
Web scraper HTML data parsed using the Beautiful Soup library.

## Usage

### Collect Current Team Statistics

Run the following command to generate a file with statistics for each team in D1 NCAAB:</br>
`$ python StatsScraper.py`</br></br>

To change what statistics are collected, edit lines 5-7 of StatsScraper.py:</br>
```python
statsToCollect = ["offensive-efficiency", "defensive-efficiency"]
statsBeginYear = 2024
statsEndYear = 2024
```
Statistics are collected from teamrankings.com. A full list of team stats can be found [here](https://www.teamrankings.com/ncb/team-stats/).

### Collect Game Data for Network Training

Run the following command to generate a file with every D1 NCAAB game played:</br>
`$ python GameDataScraper.py`</br></br>

Currently, this script only collects game data for 2024.

### Generate Training Data from Collected Games and Statistics

Run the following command to generate files with training data:</br>
`$ python GenerateTrainingData.py`</br></br>

This script generates training inputs and expected outputs using the stat and game files generated in previous steps. It looks up each team in a given game and replaces the team name with their statistics in the input file. It then takes the point differential and turns it into a 1 (first team won) or -1 (second team won) in the expected output file.</br></br>

The Names.py script was created to help map names from game data on ncaa.com to stat data on teamrankings.com. The script generates a file of all names used on each website. These names then must be manually entered into the dictionary in the GenerateTrainingData script. This step has already been completed, but you may wish to change what teams are used. If a team is not found in the dictionary, any games encountered featuring that team are skipped in the training step.

### Train the Network and Predict March Madness

Run the following command to train the network and predict March Madness:</br>
`$ python MarchMadness.py`</br></br>

Note the March Madness bracket must be manually entered at the end of the GenerateTrainingData script.</br></br>

Network parameters can be changed in lines 12-14 of the MarchMadness script:
```python
numEpochs = 100
learningRate = 0.1
networkArchitecture = [4, 50, 25, 1]
```


<!-- TODO: Better method of dictionary building for name mapping? -->
<!-- TODO: User prompts for which stats to collect, network parameters, etc. -->
<!-- TODO: Separate scripts for training and predicting - save weights in a file somewhere -->