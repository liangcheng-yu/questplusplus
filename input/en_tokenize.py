from nltk.tokenize import word_tokenize

print("Test...")
data = "All work and no play makes jack a dull boy, all work and no play"
data = data.lower()
print(word_tokenize(data))

import os

filenames = os.listdir("en_text_raw")
filenames.sort()
print(filenames)

# lowercase + tokenize
# with open('my_en_corpus.txt', 'w', encoding="utf-16") as outfile:
for fname in filenames:
    with open("en_text_raw/"+fname, 'r', encoding='utf-16') as infile:
        with open("en_text/"+fname, 'w', encoding="utf-8") as outfile:
            print("Read " + fname)
            lines = infile.readlines()
            for line in lines:
                line = line.lower()
                line = word_tokenize(line)
                line = " ".join(line)
                outfile.write(line)
                outfile.write("\n")