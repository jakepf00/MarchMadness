import csv

statNames = []
statFile = open("Stats/2024.csv", "r")
statsReader = csv.reader(statFile)
for row in statsReader:
    statNames.append(row[0])
statFile.close()

gameNames = []
gameFile = open("Games/2024.csv", "r")
gameReader = csv.reader(gameFile)
for row in gameReader:
    if row[0] not in gameNames:
        gameNames.append(row[0])
    if row[1] not in gameNames:
        gameNames.append(row[1])
gameFile.close()


statNames.sort()
gameNames.sort()

nameFile = open("names.txt", "w")
for name in gameNames:
    nameFile.write(name + "\n")
nameFile.close()

nameFile = open("names2.txt", "w")
for name in statNames:
    nameFile.write(name + "\n")
nameFile.close()

#for i in range(0, len(gameNames)):
    #nameFile.write("\"\": \"" + statNames[i] + "\",\n") # Format for dictionary conversion