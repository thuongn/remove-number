import os, glob
import re
os.chdir("alphabet")

for file in glob.glob("*.jpg"):
    os.rename(file, re.sub(r'\d+', '', file))
    print (file)
