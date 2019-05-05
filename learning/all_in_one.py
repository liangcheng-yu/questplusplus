# Run the experiments to get the average results of the svr learning (baseline, extra features, my benchmark)

import os
import json
import math
import statistics

# Number of experiments with different random seeds for each feature set
numSeeds = 10
seedPool = [i for i in range(numSeeds)]
seedPool = [1000, 3000, 5000, 7000, 1994, 2018, 2019, 19941005, 19971205, 20190505]
# Number of feature sets (excluding baseline)
numFeatureSets = 11+2
numMetrics = 4

# List of lists to store the results for baseline and each feature set (in terms of r-value, p-value, MAE, RSME metrics)
result = [[0 for _ in range(numMetrics)] for _ in range(numFeatureSets+1)]
print("Initialized results...")
for item in result:
    print(item)

# ===================================
# Baseline run
# ===================================
# What is the outputDir
outputDir = "data/result/baseline/"

print(os.system('pwd'))
os.system('ls')

# Run each experiment to obtain the resuilting json file
rowIndex = 0
for runIdx in range(numSeeds):
    os.chdir('/Users/liangchengyu/questplusplus/learning/data/features')
    os.system('ls')
    os.system('python3 cook_random_setting.py'+' --seed '+str(seedPool[runIdx]))
    os.chdir('/Users/liangchengyu/questplusplus/learning/')
    os.system("python src/learn_model.py config/svr_baseline.cfg --outputDir "+outputDir+" --seed "+str(seedPool[runIdx]))

# Iterate the json file and get the averaging result
pearson_rs = []
pearson_ps = []
MAEs = []
RMSEs = []
for seed in seedPool:
    with open(outputDir+str(seed), "r") as f:
        outputDict = json.load(f)
    print("The loaded json output: {}".format(outputDict))
    pearson_rs.append(outputDict['pearson_r'])
    pearson_ps.append(outputDict['pearson_p'])
    MAEs.append(outputDict['MAE'])
    RMSEs.append(outputDict['RMSE'])
print("=> Baseline: all pearson_corrcoefs r values: {}".format(pearson_rs))
print("=> Baseline: all pearson_corrcoefs p values: {}".format(pearson_ps))
print("=> Baseline: all MAEs: {}".format(MAEs))
print("=> Baseline: all RMSEs: {}".format(RMSEs))
print("=> Baseline: average r: {}".format(statistics.mean(pearson_rs)))
print("=> Baseline: average p: {}".format(statistics.mean(pearson_ps)))
print("=> Baseline: average MAE: {}".format(statistics.mean(MAEs)))
print("=> Baseline: average RMSE: {}".format(statistics.mean(RMSEs)))
result[rowIndex][0] = statistics.mean(pearson_rs)
result[rowIndex][1] = statistics.mean(pearson_ps)
result[rowIndex][2] = statistics.mean(MAEs)
result[rowIndex][3] = statistics.mean(RMSEs)

# ===================================
# Run extra features one by one
# ===================================
extraFeatureIndices = [
    1007,
    1017,
    1003,
    1005,
    1019,
    1021,
    1076,
    1088,
    1090,
    1083,
    1084,
    10000,
    10001,
]
# extraFeatureIndices = [
#     1017
# ]

# Run each experiment to obtain the resuilting json file
for featureIndex in extraFeatureIndices:
    rowIndex += 1
    outputDir = "data/result/"+str(featureIndex)+"/"
    for runIdx in range(numSeeds):
        os.chdir('/Users/liangchengyu/questplusplus/learning/data/features')
        os.system('ls')
        os.system('python3 cook_random_setting.py'+' --seed '+str(seedPool[runIdx])+' --label '+str(featureIndex))
        os.chdir('/Users/liangchengyu/questplusplus/learning/')
        os.system("python src/learn_model.py config/svr_"+str(featureIndex)+".cfg --outputDir "+outputDir+" --seed "+str(seedPool[runIdx]))

    # Iterate the json file and get the averaging result
    pearson_rs = []
    pearson_ps = []
    MAEs = []
    RMSEs = []
    for seed in seedPool:
        with open(outputDir+str(seed), "r") as f:
            outputDict = json.load(f)
        print("The loaded json output: {}".format(outputDict))
        pearson_rs.append(outputDict['pearson_r'])
        pearson_ps.append(outputDict['pearson_p'])
        MAEs.append(outputDict['MAE'])
        RMSEs.append(outputDict['RMSE'])
    print("=> All pearson_corrcoefs r values: {}".format(pearson_rs))
    print("=> All pearson_corrcoefs p values: {}".format(pearson_ps))
    print("=> All MAEs: {}".format(MAEs))
    print("=> All RMSEs: {}".format(RMSEs))
    print("=> Average r: {}".format(statistics.mean(pearson_rs)))
    print("=> Average p: {}".format(statistics.mean(pearson_ps)))
    print("=> Average MAE: {}".format(statistics.mean(MAEs)))
    print("=> Average RMSE: {}".format(statistics.mean(RMSEs)))
    result[rowIndex][0] = statistics.mean(pearson_rs)-result[0][0]
    # if result[rowIndex][0]>0:
        # result[rowIndex][0] = "+"+str(result[rowIndex][0])
    result[rowIndex][1] = statistics.mean(pearson_ps)-result[0][1]
    # if result[rowIndex][1]>0:
        # result[rowIndex][1] = "+"+str(result[rowIndex][1])
    result[rowIndex][2] = statistics.mean(MAEs)-result[0][2]
    # if result[rowIndex][2]>0:
        # result[rowIndex][2] = "+"+str(result[rowIndex][2])
    result[rowIndex][3] = statistics.mean(RMSEs)-result[0][3]
    # if result[rowIndex][3]>0:
        # result[rowIndex][3] = "+"+str(result[rowIndex][3])

print("===========================")
print("Check the result in one table")
print("===========================")
for item in result:
    print(item)

print("===========================")
print("Our benchmark")
print("===========================")
outputDir = "data/result/my/"
for runIdx in range(numSeeds):
    os.chdir('/Users/liangchengyu/questplusplus/learning/data/features')
    os.system('ls')
    os.system('python3 cook_random_setting.py'+' --seed '+str(seedPool[runIdx])+' --label my')
    os.chdir('/Users/liangchengyu/questplusplus/learning/')
    os.system("python src/learn_model.py config/svr_my.cfg --outputDir "+outputDir+" --seed "+str(seedPool[runIdx]))

# Iterate the json file and get the averaging result
pearson_rs = []
pearson_ps = []
MAEs = []
RMSEs = []
for seed in seedPool:
    with open(outputDir+str(seed), "r") as f:
        outputDict = json.load(f)
    print("The loaded json output: {}".format(outputDict))
    pearson_rs.append(outputDict['pearson_r'])
    pearson_ps.append(outputDict['pearson_p'])
    MAEs.append(outputDict['MAE'])
    RMSEs.append(outputDict['RMSE'])
print("=> All pearson_corrcoefs r values: {}".format(pearson_rs))
print("=> All pearson_corrcoefs p values: {}".format(pearson_ps))
print("=> All MAEs: {}".format(MAEs))
print("=> All RMSEs: {}".format(RMSEs))
print("=> Average r: {}".format(statistics.mean(pearson_rs)))
print("=> Average p: {}".format(statistics.mean(pearson_ps)))
print("=> Average MAE: {}".format(statistics.mean(MAEs)))
print("=> Average RMSE: {}".format(statistics.mean(RMSEs)))