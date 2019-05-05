# Given the feature set and the labels, cook the result train and test set

import numpy as np
import argparse

numInstances = 67
seed = 19971205
seed = 1997
seed = 20181005
seed = 1994
seed = 199410
seed = 101994
seed = 19941005
numTrainInstances = 50
numTestInstances = numInstances - numTrainInstances

parse = argparse.ArgumentParser(description='Cook the training and testing set.')
parse.add_argument(
    "-s",
    "--seed",
    default=12345,
    help="seed to run the unseen scenarios")
parse.add_argument("-numTrain", "--numTrain", default=100, help="number of training sampless")
parse.add_argument("-numTest", "--numTest", default=100, help="number of testing sampless")
parse.add_argument("-label", "--label", default="baseline")
args = parse.parse_args()

print("Set random seed: {}".format(str(args.seed)))
np.random.seed(int(args.seed))

poolIndices = [i for i in range(numInstances)]
print(poolIndices)

# Cook train indices
numTmpTrainIndices = 0
trainIndices = []
while True:
    if numTmpTrainIndices == numTrainInstances:
        break
    tmpIdx = np.random.choice(poolIndices, 1)
    if tmpIdx not in trainIndices:
        trainIndices.append(int(tmpIdx))
        numTmpTrainIndices += 1

# Cook test indices
testIndices = []
for i in poolIndices:
    if i not in trainIndices:
        testIndices.append(int(i))

trainIndices.sort()
testIndices.sort()
print("=== Result indices ===")
print("Train indices")
print(trainIndices)
print("Length: {}".format(len(trainIndices)))
print("Test indices")
print(testIndices)
print("Length: {}".format(len(testIndices)))

# Sample the original feature set and label set to obtain the result train and test set

# Generate the train and test samples for baseline, trimmed, and our method
inputDirName = args.label+"_raw"
outputDirName = args.label+"_cooked"

inputFeatureFile = "feature"
inputLabelFile = "label"
outputTrainFeatureFile = "train.qe.tsv"
outputTrainLabelFile = "train.effort"
outputTestFeatureFile = "test.qe.tsv"
outputTestLabelFile = "test.effort"

with open(inputDirName+"/"+inputFeatureFile, 'r', encoding='utf-8') as inputFile:
    with open(outputDirName+"/"+outputTrainFeatureFile, 'w', encoding="utf-8") as trainFile:
        with open(outputDirName+"/"+outputTestFeatureFile, 'w', encoding="utf-8") as testFile:
            lines = inputFile.readlines()
            lineIdx = 0
            for line in lines:
                if lineIdx in trainIndices:
                    trainFile.write(line)
                    # trainFile.write("\n")
                else:
                    testFile.write(line)
                lineIdx += 1

with open(inputDirName+"/"+inputLabelFile, 'r', encoding='utf-8') as inputFile:
    with open(outputDirName+"/"+outputTrainLabelFile, 'w', encoding="utf-8") as trainFile:
        with open(outputDirName+"/"+outputTestLabelFile, 'w', encoding="utf-8") as testFile:
            lines = inputFile.readlines()
            lineIdx = 0
            for line in lines:
                if lineIdx in trainIndices:
                    trainFile.write(line)
                    # trainFile.write("\n")
                else:
                    testFile.write(line)
                lineIdx += 1