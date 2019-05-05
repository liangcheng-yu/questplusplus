# -*- coding:utf8 -*-
# Query Stanford Parser online to obtain the mean dependency distance calculation


import os
import re
import time

from bs4 import BeautifulSoup
import json
import requests


languageSet = ["English", "Chinese"]
url = 'http://nlp.stanford.edu:8080/parser/index.jsp'


def TimeIt(method):
    def Timed(*args, **kw):
        t1 = time.time()
        result = method(*args, **kw)
        t2 = time.time()
        t3 = t2 - t1
        print(
            "{} spent {} seconds to run!".format(
                method.__name__, t3))
        return result
    return Timed


def ParseHtml(text):
    soup = BeautifulSoup(text, 'html.parser')
    tags = soup.find_all('pre')
    tag = tags[-1]
    lines = tag.text.splitlines()
    numTokens = len(lines)
    depDistanceSum = 0
    for line in lines:
        # Excluding ROOT
        if line:
            if not re.search("ROOT",line):
                try:
                    numStrs = re.findall("\d+", line)
                    print(line)
                    print(numStrs)
                    index2 = int(numStrs[-1])
                    index1 = int(re.findall(r"-(.+?),", line)[0])
                    depDistanceSum += abs(index1-index2)
                except:
                    pass
    print("Token number: {0}, dependency distance sum: {1}".format(numTokens, depDistanceSum))
    return numTokens, depDistanceSum


@TimeIt
def FetchSentenceQueryRes(sentence, language="English"):
    payLoad = {'query':sentence, 'parserSelect':language}
    if language in languageSet:
        r = requests.post(url, data=payLoad)
    else:
        raise ValueError("Unsupported language!")
    numTokens, depDistanceSum = ParseHtml(r.text)
    return numTokens, depDistanceSum
    # print(r.encoding)


print("=== Test samples ===")
# FetchSentenceQueryRes("I love writing thesis very much .", "English")
# FetchSentenceQueryRes("我 非常 爱 写 论文 .", "Chinese")
FetchSentenceQueryRes("截至 2015 年 六月 底 , 全国 机动车 保有量 达 2.7 亿 余辆 , 其中 汽车 163 亿辆 . ", "Chinese")

sourceDir = "/Users/liangchengyu/questplusplus/input/ch_text_ordered/"
targetDir = "/Users/liangchengyu/questplusplus/input/en_text_ordered/"

# print("=== Process source texts ===")
# filenames = os.listdir(sourceDir) # unordered
# filenames.sort()
# with open('sourceDepDistance.txt', 'w', encoding="utf-8") as outfile:
#     for filename in filenames:
#         docDepDistanceSum = 0.0
#         docNumTokens = 0.0
#         numSentences = 0
#         with open(sourceDir+filename, 'r', encoding='utf-8') as infile:
#             print(sourceDir+filename)
#             lines = infile.readlines()
#             for line in lines:
#                 numSentences += 1
#                 numTokens, depDistanceSum = FetchSentenceQueryRes(line, "Chinese")
#                 docDepDistanceSum += depDistanceSum
#                 docNumTokens += numTokens
#         print("Doc {0} with {1} sentences, mean dependency distance: {2}".format(filename, numSentences, docDepDistanceSum/(docNumTokens-numSentences)))
#         outfile.write(str(docDepDistanceSum/(docNumTokens-numSentences))+"\n")

print("=== Process target texts ===")
filenames = os.listdir(targetDir) # unordered
filenames.sort()
with open('targetDepDistance.txt', 'w', encoding="utf-8") as outfile:
    for filename in filenames:
        docDepDistanceSum = 0.0
        docNumTokens = 0.0
        numSentences = 0
        with open(targetDir+filename, 'r', encoding='utf-8') as infile:
            print(targetDir+filename)
            lines = infile.readlines()
            for line in lines:
                numSentences += 1
                numTokens, depDistanceSum = FetchSentenceQueryRes(line, "English")
                docDepDistanceSum += depDistanceSum
                docNumTokens += numTokens
        print("Doc {0} with {1} sentences, mean dependency distance: {2}".format(filename, numSentences, docDepDistanceSum/(docNumTokens-numSentences)))
        outfile.write(str(docDepDistanceSum/(docNumTokens-numSentences))+"\n")