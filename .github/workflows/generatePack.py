import os, zipfile
from os.path import basename


def zipme(items):
    os.chdir('build')
    if 'SorrowPack.zip' in os.listdir():
        index = 0
        while 'SorrowPack_0.{}.zip'.format(index) in os.listdir():
            index += 1
        os.rename('SorrowPack.zip', 'SorrowPack_0.{}.zip'.format(index))
    os.chdir('..')
    with zipfile.ZipFile('build/SorrowPack.zip', 'w') as thisFile:
        for item in items:
            if '.' not in item:
                for folderName, subFolders, fileNames in os.walk(item):
                    for fileName in fileNames:
                        filePath = os.path.join(folderName, fileName)
                        thisFile.write(filePath)
            else:
                thisFile.write(item)
    

zipme( ['pack.png', 'pack.mcmeta', 'assets'] )