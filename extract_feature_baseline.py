# Run this to obtain the extracted data for the baseline

import os

QUEST_DIR = "/Users/liangchengyu/questplusplus/"
print("Current dir:")
print(os.system('pwd'))
os.system('ant -v && java -cp QuEst++.jar shef.mt.DocLevelFeatureExtractor -case no -lang chinese english -input input/source.doc-level.ch input/target.doc-level.en -config config/baseline.doc-level.properties')
print("Copy the extracted feature output...")
os.system("cp "+QUEST_DIR+"output/mytest/output.txt "+QUEST_DIR+"learning/data/features/baseline_raw/feature")
print("All set!")