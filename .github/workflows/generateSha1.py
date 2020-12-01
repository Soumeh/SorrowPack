import os, hashlib, json
BLOCKSIZE = 65536

def getSha1(item):
    hasher = hashlib.sha1()
    with open(item, 'rb') as thisFile:
        buf = thisFile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = thisFile.read(BLOCKSIZE)
    return hasher.hexdigest()

def makeJson(Sha1):
    os.chdir('build')
    with open('Sha1.json', 'w+') as thisFile:
        thisDict = {'Sha1': Sha1}
        json.dump(thisDict, thisFile)

Sha1 = getSha1('build/SorrowPack.zip')
makeJson(Sha1)