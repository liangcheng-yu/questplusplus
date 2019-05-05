# Run the experiments to get the average results of the svr learning (baseline, extra features, my benchmark)

import os
import json
import math
import statistics

# Number of experiments with different random seeds for each feature set
seed = 1994
# seed = 1997
# seed = 19971205
# seed = 19941005
# seed = 2019
seed = 2020

truthScore = []
baselineScore = []
myScore = []

# ===================================
# Baseline run
# ===================================
# What is the outputDir
outputDir = "data/result/baseline/"

print(os.system('pwd'))
os.system('ls')

# Run each experiment to obtain the resuilting json file
os.chdir('/Users/liangchengyu/questplusplus/learning/data/features')
os.system('ls')
os.system('python3 cook_random_setting.py'+' --seed '+str(seed))
os.chdir('/Users/liangchengyu/questplusplus/learning/')
os.system("python src/learn_model.py config/svr_baseline.cfg --outputDir "+outputDir+" --seed "+str(seed))

# Read the truthScore and baselineScore
with open("predicted.csv", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.split()
        truthScore.append(float(line[0]))
        baselineScore.append(float(line[1]))
print(truthScore)
print(baselineScore)

print("===========================")
print("Our benchmark")
print("===========================")
outputDir = "data/result/my/"
os.chdir('/Users/liangchengyu/questplusplus/learning/data/features')
os.system('ls')
os.system('python3 cook_random_setting.py'+' --seed '+str(seed)+' --label my')
os.chdir('/Users/liangchengyu/questplusplus/learning/')
os.system("python src/learn_model.py config/svr_my.cfg --outputDir "+outputDir+" --seed "+str(seed))

# Read the truthScore and baselineScore
with open("predicted.csv", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.split()
        myScore.append(float(line[1]))
print(myScore)
# ===================================
# Plot the curve
# ===================================
""" Compare the exploration w.r.t. certain metric with canonical ones. """
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker
from matplotlib.backends.backend_pdf import PdfPages

csfont = {'fontname': 'Times New Roman'}
colors = {'bg': '0.4',
          'emph': '0.1'}
plot_name = "test"

params = {'backend': 'ps',
          'axes.labelsize': 12,
          'legend.fontsize': 12,
          'xtick.labelsize': 12,
          'ytick.labelsize': 12,
          'font.size': 12,
          'font.family': 'times new roman'}

plt.rcParams.update(params)
plt.axes([0.12, 0.32, 0.85, 0.63], frameon=True)
plt.rc('pdf', fonttype=42)  # IMPORTANT to get rid of Type 3
linestyles = ['-', '--', '-.']

marker_list = ["o", "v", "^", "<", ">", "8", "s", "p", "P", "*", "H", "X", "d", "_", "|", "x", "+", "4", "3", "2", "1"]
colors     = ['0.3', '0.1', '0.0']
colorIdx = 0

plt.plot(truthScore,
            linestyle='-', label="Truth", color='crimson', marker="x")
colorIdx += 1
plt.plot(myScore,
            linestyle='-', label="Proposed", color=colors[colorIdx], marker="o")
colorIdx += 1

plt.plot(baselineScore, linestyle='-.',  color=colors[colorIdx], label='Baseline', marker="s")
plt.ylabel('Score [0-100]', **csfont, fontsize=12)
plt.xlabel('Text Index', **csfont, fontsize=12)
plt.legend(
    bbox_to_anchor=(
        0.96,
        0.8),
    loc='lower right',
    ncol=2,
    columnspacing=0.6,
    borderpad=0.3)
plt.grid(True, linestyle=':', color='0.6', zorder=0, linewidth=1.2)

# plt.show()
plt.savefig(
    "{}.png".format(plot_name),
    bbox_inches='tight',
    format='png',
    dpi=800)
