# Run this to obtain the extracted datas for our feature sets
import os

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
]

QUEST_DIR = "/Users/liangchengyu/questplusplus/"
print("Current dir:")
print(os.system('pwd'))
os.system("ant -v")

# Run the feature extraction for each extra feature based on the baseline...
for index in extraFeatureIndices:
    # os.system("rm -rf input/mytest/ && ant -v && java -cp QuEst++.jar shef.mt.DocLevelFeatureExtractor -case no -lang chinese english -input input/source.doc-level.ch input/target.doc-level.en -config config/my.doc-level.properties")
    os.system("java -cp QuEst++.jar shef.mt.DocLevelFeatureExtractor -case no -lang chinese english -input input/source.doc-level.ch input/target.doc-level.en -config config/"+str(index)+".doc-level.properties")
    print("Copy the extracted feature output...")
    os.system("cp "+QUEST_DIR+"output/mytest/output.txt "+QUEST_DIR+"learning/data/features/"+str(index)+"_raw/feature")

# Run the combined feature set
os.system("java -cp QuEst++.jar shef.mt.DocLevelFeatureExtractor -case no -lang chinese english -input input/source.doc-level.ch input/target.doc-level.en -config config/my.doc-level.properties")
print("Copy the extracted feature output...")
os.system("cp "+QUEST_DIR+"output/mytest/output.txt "+QUEST_DIR+"learning/data/features/my_raw/feature")


print("All set!")