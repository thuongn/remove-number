import os, glob

os.chdi("/alphabet")

for file in glob.glob("*.jpg"):
    print (file)
