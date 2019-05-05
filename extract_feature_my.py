# Run this to obtain the extracted datas for our feature sets
import os

# Toggle extra features
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
# Assume prior offline extraction run
withSourceDep = True  # Index 10000
withTargetDep = True  # Index 10001

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

# Merge the dependency related features with the baseline features repectively
os.system('ant -v && java -cp QuEst++.jar shef.mt.DocLevelFeatureExtractor -case no -lang chinese english -input input/source.doc-level.ch input/target.doc-level.en -config config/baseline.doc-level.properties')
if withSourceDep:
    with open(QUEST_DIR+"learning/data/features/10000_raw/feature", 'w', encoding="utf-8") as outfile:
        with open(QUEST_DIR+"output/mytest/output.txt", 'r', encoding='utf-8') as infileBaseline:
            with open(QUEST_DIR+"sourceDepDistance.txt", 'r', encoding='utf-8') as infileSource:
                linesBaseline = infileBaseline.readlines()
                linesSource = infileSource.readlines()
                if len(linesBaseline)==len(linesSource):
                    for idx in range(len(linesBaseline)):
                        lineW = linesBaseline[idx].strip('\n')+"\t"+linesSource[idx]
                        outfile.write(lineW)
if withTargetDep:                        
    with open(QUEST_DIR+"learning/data/features/10001_raw/feature", 'w', encoding="utf-8") as outfile:
        with open(QUEST_DIR+"output/mytest/output.txt", 'r', encoding='utf-8') as infileBaseline:
            with open(QUEST_DIR+"targetDepDistance.txt", 'r', encoding='utf-8') as infileTarget:
                linesBaseline = infileBaseline.readlines()
                linesTarget = infileTarget.readlines()
                if len(linesBaseline)==len(linesTarget):
                    for idx in range(len(linesBaseline)):
                        lineW = linesBaseline[idx].strip('\n')+"\t"+linesTarget[idx]
                        outfile.write(lineW)

# Run the combined feature set
os.system("java -cp QuEst++.jar shef.mt.DocLevelFeatureExtractor -case no -lang chinese english -input input/source.doc-level.ch input/target.doc-level.en -config config/my.doc-level.properties")
print("Copy the extracted feature output...")
os.system("cp "+QUEST_DIR+"output/mytest/output.txt "+QUEST_DIR+"learning/data/features/my_raw/feature")


print("All set!")