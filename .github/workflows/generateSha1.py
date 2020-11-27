import os, hashlib, jsonBLOCKSIZE = 65536os.chdir('..')
os.chdir('..')def getSha1(item):    hasher = hashlib.sha1()    with open(item, 'rb') as thisFile:        buf = thisFile.read(BLOCKSIZE)        while len(buf) > 0:            hasher.update(buf)            buf = thisFile.read(BLOCKSIZE)    return hasher.hexdigest()def makeJson(Sha1):    os.chdir('build')
    if 'Sha1.json' in os.listdir():
        index = 0
        while 'Sha1_{}.json'.format(index) in os.listdir():
            index += 1
        os.rename('Sha1.json', 'Sha1_{}.json'.format(index))    with open('Sha1.json', 'w') as thisFile:        thisDict = {'Sha1': Sha1}        json.dump(thisDict, thisFile)Sha1 = getSha1('build/SorrowPack.zip')makeJson(Sha1)