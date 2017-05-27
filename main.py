import os, glob

os.chdir("alphabet")

for file in glob.glob("*.jpg"):
    print (file)
