import hashlib
import os

def computeMD5hash(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()

if not os.path.exists("md5/"):
    os.makedirs("md5/")

for root,dirs,files in os.walk('.'):
    for file in files:
        if '.txt' in file:
            with open(file) as f:
                md5_string = computeMD5hash(f.read())
                f1 = open("md5/"+file, 'w')
                f1.write(md5_string)
                f1.close()