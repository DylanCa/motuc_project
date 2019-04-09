from functions.filefunctions import FileFunction
from string import ascii_lowercase
from itertools import cycle

import json


class FrequencyAnalysis():
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def initfile(self, filename):
        EncryptedFileFunctions = FileFunction(filename)
        return EncryptedFileFunctions.openfile()

    def analysefrequencyandgetkey(self, encrypted_file, keylength):
        blocks, frequencytab = {}, {}

        for x in range(0, keylength):
            blocks[x] = []
            frequencytab[x] = {}

        i = 0

        for x, char in zip(
                cycle(range(0, keylength)), ''.join(encrypted_file)):
            blocks[x].append(char)

        highestEfreq = 0
        key = ""
        _tempkey = ""

        for i, block in enumerate(blocks):
            for l in ascii_lowercase:
                frequencytab[i][l] = {}
                for char in blocks[i]:
                    val = chr(ord(char) ^ ord(l))
                    frequencytab[i][l][val] = frequencytab[i][l].get(val,
                                                                     0) + 1

                for index in frequencytab[i][l]:
                    frequencytab[i][l][index] = {
                        'count': frequencytab[i][l][index],
                        'freq':
                        frequencytab[i][l][index] / len(blocks[i]) * 100
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

        return frequencytab['finalkey']
