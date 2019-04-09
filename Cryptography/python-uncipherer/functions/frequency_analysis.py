from filefunctions import FileFunction
from string import ascii_lowercase

import json

EncryptedFileFunctions = FileFunction("PA.txt")
encrypted_file = EncryptedFileFunctions.openfile()

blocks = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
frequencytab = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}}

i = 0

for char in ''.join(encrypted_file):
    blocks[i].append(char)
    i = i + 1 if i < 5 else 0

highestEfreq = 0
key = ""
_tempkey = ""

for i, block in enumerate(blocks):
    for l in ascii_lowercase:
        frequencytab[i][l] = {}
        for char in blocks[i]:
            val = chr(ord(char) ^ ord(l))
            frequencytab[i][l][val] = frequencytab[i][l].get(val, 0) + 1

        for index in frequencytab[i][l]:
            frequencytab[i][l][index] = {
                'count': frequencytab[i][l][index],
                'freq': frequencytab[i][l][index] / len(blocks[i]) * 100
            }
        try:
            if frequencytab[i][l]['e']['freq'] > highestEfreq:
                highestEfreq = frequencytab[i][l]['e']['freq']
                _tempkey = l
        except Exception:
            pass

    key += _tempkey
    highestEfreq = 0

frequencytab['finalkey'] = key

print(json.dumps(frequencytab))
print("The decrypt key for this file is >>{}<<".format(
    frequencytab['finalkey']))
