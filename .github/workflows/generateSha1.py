import os, hashlib, json
    if 'Sha1.json' in os.listdir():
        index = 0
        while 'Sha1_{}.json'.format(index) in os.listdir():
            index += 1
        os.rename('Sha1.json', 'Sha1_{}.json'.format(index))