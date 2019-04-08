from filefunctions import FileFunction
from string import ascii_lowercase

import json

EncryptedFileFunctions = FileFunction("../encrypted_files/PB0.txt")
encrypted_file = EncryptedFileFunctions.openfile()

key = ''
i = 0
filelen = 0

blocks = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
frequencytab = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}}
for char in ''.join(encrypted_file):
    filelen += 1
    blocks[i].append(char)
    i = i + 1 if i < 5 else 0

for letter in ascii_lowercase:
    for index, block in enumerate(blocks):
        frequencytab[index][letter] = {}
        for char in blocks[index]:
            val = chr(ord(char) ^ ord(letter))
            frequencytab[index][letter][val] = frequencytab[index][letter].get(
                val, 0) + 1

for i in frequencytab:
    highestEfreq = 0
    lowestWfreq = 100
    keyletter = ''
    for l in frequencytab[i]:
        for v in frequencytab[i][l]:
            frequencytab[i][l][v] = {
                'count': frequencytab[i][l][v],
                'freq': round((frequencytab[i][l][v] / (filelen - 1)) * 100, 2)
            }

        try:
            if frequencytab[i][l]["e"]['freq'] > highestEfreq and frequencytab[
                    i][l]["w"]['freq'] < lowestWfreq:
                highestEfreq = frequencytab[i][l]["e"]['freq']
                lowestWfreq = frequencytab[i][l]["w"]['freq']
                keyletter = l
        except Exception:
            pass
    frequencytab[i]["result"] = {
        "block#": i,
        "HighestEFreq": highestEfreq,
        "LowestWFreq": lowestWfreq,
        "keyletter": keyletter
    }
    key += keyletter

frequencytab['key'] = key
print(json.dumps(frequencytab))
